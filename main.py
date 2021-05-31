# -*- coding: utf-8 -*-
"""
@author: Benoît Etienne, Alexandre Bosch
"""

from decompression import get_path_folder
from visualisation import print_scatter, get_PCA, print_PCA_2D, print_PCA_3D, print_t_SNE
from classification import create_dataframe, create_model


# function to classify and visualise the dataset
def classify_visualise(folder_name, targets, list_drop = [], nb_cluster = 3, random = False, samples = 0, scatter = True, PCA_2D = True, PCA_3D = True, graph_2D = True, graph_3D = True, t_SNE = True):
    path = get_path_folder(folder_name)
    
    df = create_dataframe(path, folder_name, list_drop)
    
    if scatter:
        print_scatter(df, folder_name)
    
    if PCA_2D or PCA_3D or t_SNE or graph_2D or graph_3D:
        for target in targets :
            X, y, model, y_pred = create_model(df, target, nb_cluster, random, samples)
            
            if PCA_2D or PCA_3D or t_SNE:
                    X_pca, pca_result = get_PCA(X)
                    
                    if PCA_2D:
                        print_PCA_2D(X_pca, folder_name, target)
                    
                    if PCA_3D and len(X.columns) < 3:
                        print_PCA_3D(X_pca, y, folder_name, target) 
                        print_PCA_3D(X_pca, y_pred, folder_name, target) 
                    
                    if t_SNE:
                        print_t_SNE(X_pca, pca_result, folder_name, target)



# drop the column "missing info" because it has NaN values
# drop the columns "missing info", "user", "job name" and "logical job name" because they have STRING_HASH values
job_events_drop = ["missing info", "user", "job name", "logical job name"]
job_events_targets = ["time", "job ID", "event type", "scheduling class"]
# classify_visualise("job_events", job_events_targets, job_events_drop, scatter = False, PCA_2D = False, PCA_3D = False, t_SNE = False)
# classify_visualise("job_events", job_events_targets, job_events_drop, PCA_2D = False, PCA_3D = False, graph_2D = False, graph_3D = False, t_SNE = False)

classify_visualise("job_events", job_events_targets, job_events_drop, t_SNE = False)
# sampling 10 000 sample to avoid memory errors for the t-SNE and to have a more interresting plot
classify_visualise("job_events", job_events_targets, job_events_drop, random = True, samples = 10000, scatter = False, PCA_2D = False, PCA_3D = False)



# drop the columns "attribute name" and "attribute value" because they have STRING_HASH values
task_constraints_drop = ["attribute name","attribute value"]
task_constraints_targets = ["time","job ID","task index","comparison operator"]

classify_visualise("task_constraints", task_constraints_targets, task_constraints_drop, PCA_3D = False, t_SNE = False)
# sampling 100 000 sample to avoid memory errors for the 3D PCA
classify_visualise("task_constraints", task_constraints_targets, task_constraints_drop, random = True, samples = 100000, scatter = False, PCA_2D = False, t_SNE = False)
# sampling 10 000 sample to avoid memory errors for the t-SNE and to have a more interresting plot
classify_visualise("task_constraints", task_constraints_targets, task_constraints_drop, random = True, samples = 10000, scatter = False, PCA_2D = False, PCA_3D = False)


# drop the columns "attribute name" and "attribute value" because they have STRING_HASH values
machine_attributes_drop = ["attribute name","attribute value"]
machine_attributes_targets = ["time","machine ID","attribute deleted"]

classify_visualise("machine_attributes", machine_attributes_targets, machine_attributes_drop, 2, t_SNE = False)
# sampling 10 000 sample to avoid memory errors for the t-SNE and to have a more interresting plot
classify_visualise("machine_attributes", machine_attributes_targets, machine_attributes_drop, 2, random = True, samples = 10000, scatter = False, PCA_2D = False, PCA_3D = False)


# drop the column "platform ID" because it has STRING_HASH values
# drop the columns "CPUs","Memory" because they contain NaN, infinity or (a) value(s) too large for dtype('float64')
machine_events_drop = ["platform ID","CPUs","Memory"]
machine_events_targets = ["time","machine ID","event type"]

classify_visualise("machine_events", machine_events_targets, machine_events_drop, t_SNE = False)
# sampling 10 000 sample to avoid memory errors for the t-SNE and to have a more interresting plot
classify_visualise("machine_events", machine_events_targets, machine_events_drop, random = True, samples = 10000, scatter = False, PCA_2D = False, PCA_3D = False)

