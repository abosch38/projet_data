# -*- coding: utf-8 -*-
"""
@author: Benoît Etienne, Alexandre Bosch
"""

from sklearn.cluster import KMeans
from sklearn.utils import shuffle

from decompression import get_path_folder

import pandas as pd


# function creating and preparing the dataframe
def create_dataframe(path, folder_name, list_drop = []):
    df = pd.read_csv(path + "\\" + folder_name + ".csv")
    df = df.drop(columns = list_drop)
    return df



# function creating and preparing the model
def create_model(df, target, nb_cluster, random = False, samples = 0):
    if random:
        df = shuffle(df)
    
    if samples > 0 and samples < len(df):
        df = df[0:samples]
    
    X = df.drop(columns = target)   # drop the target table
    
    y = df[target]                  # create the target dataframe with the target table of the dataset
    
    model = KMeans(n_clusters = nb_cluster)
    model.fit(X, y)
    y_pred = model.predict(X)
    
    return X, y, model, y_pred


#%% create the job_events's training and testing dataframe
if __name__ == "__main__":
    path = get_path_folder("job_events")
    df_job_events = create_dataframe(path, "job_events", ["missing info", "user", "job name", "logical job name"])
    X_job_events, y_job_events, model, y_job_events_pred = create_model(df_job_events, "time")
    
    path = get_path_folder("machine_attributes")
    df_machine_attributes = create_dataframe(path, "machine_attributes", ["attribute name","attribute value"])
    X_machine_attributes, y_machine_attributes, model, y_machine_attributes_pred = create_model(df_machine_attributes, "attribute deleted")
