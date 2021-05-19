# -*- coding: utf-8 -*-
"""
@author: Benoît Etienne, Alexandre Bosch
"""

import gzip
import shutil
import os

# function returning the path of the folder
def get_path_folder(folder_name):
    folder_path = os.path.dirname(__file__)
    
    if folder_name[0] in "abfnrtuvx":
        folder_name = "\\" + folder_name
    
    path = os.path.join(folder_path, 'clusterdata-2011-2\\' + folder_name)
    
    return path


# function to decompress .gz file to .csv file
def decompress_gz_to_csv(folder_name, attributes, start = 0, end = 500):  # start is used in the case when only some files have been decompressed
    path = get_path_folder(folder_name)
    
    number_of_file = str(end)
    end_file_name = "-of-00" + "0"*(3-len(number_of_file)) + number_of_file + ".csv.gz"
    
    for i in range(start, end):
        file_number = str(i)
        file_name = path + "\part-00" + "0"*(3-len(file_number)) + file_number + end_file_name
        
        with gzip.open(file_name, 'rb') as f_in:            # open and decompress the .gz file and store it's data in f_in
            with open(file_name[:-3], 'wb') as f_out:       # open a file where we will put the data and store it in f_out
                shutil.copyfileobj(f_in, f_out)             # copy the data from f_in to f_out
        
        f = open(file_name[:-3],"r+")                       # open in read and write mode the .csv file
        text = f.read()
        f.seek(0)
        f.write(attributes + "\n" + text)                   # add the attributes at the beginning of the .csv file
        f.close()


#%% decompress the .gz files in the dataset
if __name__ == "__main__":
    decompress_gz_to_csv("job_events", "time,missing info,job ID,event type,user,scheduling class,job name,logical job name")
    
    decompress_gz_to_csv("machine_attributes", "time,machine ID,attribute name,attribute value,attribute deleted", end = 1)
    
    decompress_gz_to_csv("machine_events", "time,machine ID,event type,platform ID,CPUs,Memory", end = 1)
    
    decompress_gz_to_csv("task_constraints", "time,job ID,task index,comparison operator,attribute name,attribute value")
    
    decompress_gz_to_csv("task_events", "time,missing info,job ID,task index,machine ID,event type,user,scheduling class,priority,CPU request,memory request,disk space request,different machines restriction")
    
    decompress_gz_to_csv("task_usage", "start time,end time,job ID,task index,machine ID,CPU rate,canonical memory usage,assigned memory usage,unmapped page cache,total page cache,maximum memory usage,disk I/O time,local disk space usage,maximum CPU rate,maximum disk IO time,cycles per instruction,memory accesses per instruction,sample portion,aggregation type,sampled CPU usage")
