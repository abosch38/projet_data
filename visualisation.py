# -*- coding: utf-8 -*-
"""
@author: Benoît Etienne, Alexandre Bosh
"""

from pandas.plotting import scatter_matrix
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns



#%% print with scatter_matrix

def print_scatter(X):
    plt.figure()
    scatter_matrix(X, diagonal='kde')
    plt.show()



#%% get_PCA

def get_PCA(X):
    pca = PCA(n_components=3)
    pca_result = pca.fit_transform(X.values)
    
    X['pca-one'] = pca_result[:,0]
    X['pca-two'] = pca_result[:,1] 
    X['pca-three'] = pca_result[:,2]
    
    return X, pca_result


#%% print PCA en 2D

def print_PCA_2D(X):
    plt.figure(figsize=(16,10))
    sns.scatterplot(
        x="pca-one", y="pca-two",
        palette=sns.color_palette("hls", 10),
        data=X,
        legend="full",
        alpha=0.3
    )


#%% print PCA en 3D

def print_PCA_3D(X, Y):
    ax = plt.figure(figsize=(16,10)).gca(projection='3d')
    ax.scatter(
        xs=X['pca-one'],
        ys=X['pca-two'],
        zs=X['pca-three'],
        c=Y,
        cmap='tab10'
    )
    
    ax.set_xlabel('pca-one')
    ax.set_ylabel('pca-two')
    ax.set_zlabel('pca-three')
    plt.show()


#%%

def print_t_SNE(X, pca_result):
    tsne = TSNE(n_components=2, verbose=0, perplexity=40, n_iter=300)
    tsne_pca_results = tsne.fit_transform(pca_result)

    X['tsne-pca50-one'] = tsne_pca_results[:,0]
    X['tsne-pca50-two'] = tsne_pca_results[:,1]
    
    plt.figure()
    sns.scatterplot(
        x="tsne-pca50-one", y="tsne-pca50-two",
        palette=sns.color_palette("hls", 10),
        data=X,
        legend="full",
        alpha=0.3,
    )
    