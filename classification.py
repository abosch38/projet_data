# -*- coding: utf-8 -*-
"""
@author: Benoît Etienne, Alexandre Bosch
"""

from sklearn.cluster import KMeans
from sklearn.utils import shuffle

from decompression import get_path_folder

import pandas as pd


# function creating and preparing the dataframe and the model
def create_dataframe_model(path, folder_name, target, list_drop = [], random = False, samples = 0):
    df = pd.read_csv(path + "\\" + folder_name + ".csv")
    
    if random:
        df = shuffle(df)
    
    if samples > 0 and samples < len(df):
        df = df[0:samples]
    
    X = df.drop(columns = target)   # drop the target table
    X = X.drop(columns = list_drop)
    
    y = df[target]                  # create the target dataframe with the target table of the dataset
    
    model = KMeans(n_clusters=3)
    model.fit(X, y)
    
    return X, y, model


#%% create the job_events's training and testing dataframe
if __name__ == "__main__":
    path = get_path_folder("job_events")
    X_job_events, y_job_events, model = create_dataframe_model(path, "job_events", "time", list_drop = ["missing info", "user", "job name", "logical job name"])
