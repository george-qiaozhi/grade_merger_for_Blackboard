import csv, os
import pandas as pd 

def main():
    # configure the source and target file, and the fields to merge
    #labs = ["301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "314", "315"]
    labs = os.listdir("labSection/")
    #lectures = ["001", "002"]
    lectures = os.listdir("mainSection/")
    common_key = ["Username"] # Username is used to match student's record between lab and main section
    #avilable = ["Availability"]  # if Availability is No, skip this record
    columns_to_transfer = ["Lab 01", "Lab 02", "Lab 03", "Lab 04", "Lab 05", "Lab 06", "Lab 07", "Lab 08", "Lab 09", "Lab 10", "Lab 11", "Lab 12",
     "Quiz 01", "Quiz 02", "Quiz 03", "Quiz 04", "Quiz 05", "Quiz 06", "Quiz 07", "Quiz 08", "Quiz 09", "Quiz 10", 
     "Lab Exam 01", "Lab Exam 02", "Lab Final Exam"]
    # columns_to_transfer = ["Lab 01", "Lab 02"]
    # labs = ["301", "302", "303", "304"]
    working_fields = common_key + columns_to_transfer
    
    #format verification
    CONT = True
    for lab in labs:
        header = list(pd.read_csv(os.path.join("labSection", lab)))
        for field in working_fields:
            PASS = False
            for item in header:
                if field in item:
                    PASS = True 
            if PASS == False:
                CONT = False
                print("INVALID format at " + lab + " Expecting \'" + field + "...")
    for lec in lectures:
        header = list(pd.read_csv(os.path.join("mainSection", lec)))
        for field in working_fields:
            PASS = False
            for item in header:
                if field in item:
                    PASS = True 
            if PASS == False:
                CONT = False
                print("INVALID format at " + lec + " Expecting \'" + field + "...")

    # import source files and merge them into a single table workplace
    if(CONT):
        master_t = pd.DataFrame(columns=working_fields)
        for lab in labs:
            tmp_orgnized = pd.DataFrame(columns=working_fields)# orgnized temp file with column name from working_fields
            tmp_source = pd.read_csv(os.path.join("labSection", lab))# original file is blackboard's csv file
            for column in tmp_source:
                for f in working_fields:
                    if f in column:
                        tmp_orgnized[f] = tmp_source[column]
            master_t = master_t.append(tmp_orgnized, ignore_index=True)
        
        for lec in lectures:
            # import target file
            target_t = pd.read_csv(os.path.join("mainSection", lec))
            
            # print dropped student
            #print(target_t[~(target_t['Availability'] == 'Yes')])

            #mearge the labs to mains
            #create left table that only have Username
            tmp_target_t_left = target_t.loc[:, ['Username']]
            #print(master_t)
            tmp_target_t = pd.merge(tmp_target_t_left, master_t, how='left', on=['Username'])

            #copy grades to main
            tmp_target_t_header = list(tmp_target_t)
            target_t_header = list(target_t)
            for i in tmp_target_t_header:
                for j in target_t_header:
                    if i in j:
                        target_t[j] = tmp_target_t[i]
            #save final result to file
            ## lec[:-4] trim off .csv before adding _ready.csv
            target_t.to_csv(lec[:-4] + '_ready.csv', index=False, quoting=csv.QUOTE_ALL)
    else:
        print("ERROR: won't update anything until error fixed...")

#call functions
main()




















