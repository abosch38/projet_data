# -*- coding: utf-8 -*-
"""
@author: Benoît Etienne, Alexandre Bosh
"""

import pandas as pd
from sklearn.cluster import KMeans


#%% Function creating and preparing the dataframe and the model

def create_dataframe_model(path, folder_name, target, list_drop = []):
    df = pd.read_csv(path + "\\" + folder_name + ".csv")
    
    X = df.drop(columns = target)   # drop the target table
    for table in list_drop :
        X = X.drop(columns = table)
    
    y = df[target]                  # create the target dataframe with the target table of the dataset
    
    model = KMeans(n_clusters=3)
    model.fit(X, y)
    
    return X, y, model
