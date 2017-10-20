# Blackboard Grades Merger
This python scripts is to merge grades from CSCE1030 lab sections to main sections. It took Blackboard (BB) `.csv` file from lab sections as input, load grades into a **pandas** dataframe, then merge the grade to main section's `.csv` file.

## Dependency
Python pandas module: [Installation Guide](https://pandas.pydata.org/pandas-docs/stable/install.html)

## Prerequisite
- python (2.7 or 3+) with pandas module installed
- .csv file download from BB, in `labSection` & `mainSection` folder accordingly
- A clear mind

## How-To
This section provides a step-by-step instruction on how to use this script to merge grades to main section on BB. **Remember to backup the downloaded files before make any changes, and double check before upload.**

1. Download this project, including folders and scriptes. or via command:  `git clone https://github.com/george-qiaozhi/grade_merger_for_Blackboard`
2. On Blackboard, make sure all lab sections have the same column name. E.g., `Lab01` or `Lab 1`, `Quiz01`, and `LabExam01`. The string match is case sensitive and cannot tolerate `whitespace`. It doesn't support fuzzy match at this moment.
3. On Blackboard, go to main sections and create columns for each lab column you want to copy over. E.g., if you want to merge `Lab01`, `Lab02`, and `Quiz01` to main sections, for each main section, create `Lab01`, `Lab02`, and `Quiz01` columns. Double check column name, it needs to be matched with lab sections column name.
4. On Blackboard, go to `Grade Center > Full Grade Center > Work Offline > Download`, for "Delimiter Type" choose "comma" to download as .csv file. 
5. Repeat `Step 4` for each labs and main sections. Put labs and main sections `.csv` file into the according folder, i.e., `labSection` & `mainSection`.
6. **Backup the downloaded files to a different directory**, so you can have something to recovery from later on if you messed up.
7. Run python script `python merge.py` or use your IDE environment. It will first check formatting of the files, and prompt error if found error. Then proceed and generate `xx_ready.csv` file if no error were detected.
8. Upload `xx_ready.csv` file to Blackboard via `Grade Center > Full Grade Center > Work Offline > Upload`, after submit, it previews all the changes, **Check them carefully!** Then confirm the submission.


## Tested Environment
```
ubuntu 16.04LTS
python 3.5
```
