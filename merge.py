import csv, os
import pandas as pd 

def main():
    # read subfolder for labs and main sections source .csv file into lists
    labs = os.listdir("labSection/")
    print(labs)
    lectures = os.listdir("mainSection/")
    print(lectures)

    # Username is used to match student's record between lab and main section
    common_key = ["Username"] 

    # avilable = ["Availability"]  # if Availability is No, skip this record
    
    # the column need to transfer from lab section to main section
    columns_to_transfer = ["Lab 01", "Lab 02", "Lab 03", "Lab 04", "Lab 05", "Lab 06", "Lab 07", "Lab 08", "Lab 09", "Lab 10", "Lab 11", "Lab 12",
     "Quiz 01", "Quiz 02", "Quiz 03", "Quiz 04", "Quiz 05", "Quiz 06", "Quiz 07", "Quiz 08", "Quiz 09", "Quiz 10", 
     "Lab Exam 01", "Lab Exam 02", "Lab Final Exam"]

    # working_fields is used to create intermidiate tables
    working_fields = common_key + columns_to_transfer
    
    # format verification
    CONT = True
    for lab in labs:
    	# parse the input file header for formatting check
        header = list(pd.read_csv(os.path.join("labSection", lab)))
        # make sure input file have all the columns in columns_to_transfer  
        for field in working_fields:
            PASS = False
            for item in header:
                if field in item:
                    PASS = True 
            if PASS == False:
                CONT = False
                print("INVALID format at " + lab + ". Expecting \'" + field + "...")
    for lec in lectures:
    	# parse the input file header for formatting check
        header = list(pd.read_csv(os.path.join("mainSection", lec)))
        # make sure input file have all the columns in columns_to_transfer 
        for field in working_fields:
            PASS = False
            for item in header:
                if field in item:
                    PASS = True 
            if PASS == False:
                CONT = False
                print("INVALID format at " + lec + ". Expecting \'" + field + "...")

    # import source files and merge them into a single table workplace
    if(CONT):
    	# create the intermidiate file aka workplace
        master_t = pd.DataFrame(columns=working_fields)
        for lab in labs:
        	# orgnized input file columns to the same order as specified in 'columns_to_transfer'.
        	# each input file might have different column orders, since different TA might have 
        	# different preference to create columns. But master_t must have one unique order.
            tmp_orgnized = pd.DataFrame(columns=working_fields)
            tmp_source = pd.read_csv(os.path.join("labSection", lab))
            for column in tmp_source:
                for f in working_fields:
                    if f in column:
                        tmp_orgnized[f] = tmp_source[column]
            master_t = master_t.append(tmp_orgnized, ignore_index=True)
        
        for lec in lectures:
            target_t = pd.read_csv(os.path.join("mainSection", lec))
            
            # print dropped student
            # print(target_t[~(target_t['Availability'] == 'Yes')])

            # make temp file that merge the labs to mains use left join, table size master_t > target_t
            # create left table that following main section's Username order
            tmp_target_t_left = target_t.loc[:, ['Username']]
            tmp_target_t = pd.merge(tmp_target_t_left, master_t, how='left', on=['Username'])

            #copy grades to main
            tmp_target_t_header = list(tmp_target_t)
            target_t_header = list(target_t)
            for i in tmp_target_t_header:
                for j in target_t_header:
                    if i in j:
                        target_t[j] = tmp_target_t[i]
                        
            # save final result to file
            # lec[:-4] trim off ".csv" before adding "_ready.csv"
            target_t.to_csv(lec[:-4] + '_ready.csv', index=False, quoting=csv.QUOTE_ALL)
        print("DONE...")
    else:
        print("ERROR: won't update anything until error fixed...")

#call functions
main()




















