# -*- coding: utf-8 -*-
"""
@author: Benoît Etienne, Alexandre Bosch
"""

from decompression import get_path_folder

# this function bring in one file all the .csv files of a folder
def gather_csv(folder_name, end = "500"):  # start is used in the case when only some files have been gathered
    path = get_path_folder(folder_name)
    end_file_name = "-of-00" + "0"*(3-len(end)) + end + ".csv"
    text_main = ""
    
    file_name = path + "\part-00000" + end_file_name
    f = open(file_name,"r")
    text_main += f.read()
    f.close()
    
    for i in range(1, int(end)):
        text_main += "\n"
        file_number = str(i)
        file_name = path + "\part-00" + "0"*(3-len(file_number)) + file_number + end_file_name
        f = open(file_name,"r")
        text = f.read()
        text_main += clean_text(text)   # remove the line of the attributes
        f.close()
    
    file_name = path + "\\" + folder_name + ".csv"
    file_main = open(file_name,"a")
    file_main.write(text_main)
    file_main.close()

# this function remove the first line of the text
def clean_text(text):
    i = 1
    while not(("\n" in text[i-1:i+1])):
        i += 1
    return text[i+2:]


#%% gathering the .csv files in each folders
if __name__ == "__main__":
    gather_csv("job_events")
    
    gather_csv("machine_attributes", end = "1")
    
    gather_csv("machine_events", end = "1")
    
    gather_csv("task_constraints")
    
    gather_csv("task_events")
    
    gather_csv("task_usage")
