# -*- coding: utf-8 -*-
"""
@author: Benoît Etienne, Alexandre Bosch
"""

from decompression import get_path_folder
from visualisation import print_scatter, get_PCA, print_PCA_2D, print_PCA_3D, print_t_SNE
from classification import create_dataframe_model


# function to classify and visualise the dataset
def classify_visualise(folder_name, target, list_drop = [], random = False, samples = 0, scatter = True, PCA_2D = True, PCA_3D = True, t_SNE = True):
    path = get_path_folder(folder_name)
    
    X, y, model = create_dataframe_model(path, folder_name, target, list_drop, random, samples)
    
    if scatter:
        print_scatter(X, folder_name, target)
    
    if PCA_2D or PCA_3D or t_SNE:
        X, pca_result = get_PCA(X)
        
        if PCA_2D:
            print_PCA_2D(X, folder_name, target)
        
        if PCA_3D:
            print_PCA_3D(X, y, folder_name, target) 
        
        if t_SNE:
            print_t_SNE(X, pca_result, folder_name, target)



# drop the table "missing info" because it has NaN values
# drop the tables "missing info", "user", "job name" and "logical job name" because they have STRING_HASH values
job_events_drop = ["missing info", "user", "job name", "logical job name"]
job_events_targets = ["time", "job ID", "event type", "scheduling class"]

for target in job_events_targets:
    classify_visualise("job_events", target, job_events_drop, t_SNE = False)
    # sampling 10 000 sample to avoid memory errors for the t-SNE and to have a more interresting plot
    classify_visualise("job_events", target, job_events_drop, random = True, samples = 10000, scatter = False, PCA_2D = False, PCA_3D = False)



# drop the table "missing info" because it has NaN values
# drop the tables "missing info", "user", "job name" and "logical job name" because they have STRING_HASH values
task_constraints_drop = ["attribute name","attribute value"]
task_constraints_targets = ["time","job ID","task index","comparison operator"]

for target in task_constraints_targets:
    classify_visualise("task_constraints", target, task_constraints_drop, PCA_3D = False, t_SNE = False)
    # sampling 100 000 sample to avoid memory errors for the 3D PCA
    classify_visualise("task_constraints", target, task_constraints_drop, random = True, samples = 100000, scatter = False, PCA_2D = False, t_SNE = False)
    # sampling 10 000 sample to avoid memory errors for the t-SNE and to have a more interresting plot
    classify_visualise("task_constraints", target, task_constraints_drop, random = True, samples = 10000, scatter = False, PCA_2D = False, PCA_3D = False)
