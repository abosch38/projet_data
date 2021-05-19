# -*- coding: utf-8 -*-
"""
@author: Benoît Etienne, Alexandre Bosch
"""

from pandas.plotting import scatter_matrix
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns


# function to set the title for the graph
def get_title(graphe, table, target):
    return graphe + ' with target variable "' + target + '" from the table "' + table +'"'


# print with scatter_matrix
def print_scatter(X, table, target):
    plt.figure()
    scatter_matrix(X, diagonal='kde')
    title = get_title("Scatter", table, target)
    plt.suptitle(title)
    plt.show()


# to instantiate the PCA
def get_PCA(X):
    pca = PCA(n_components=3)
    pca_result = pca.fit_transform(X.values)
    
    X['pca-one'] = pca_result[:,0]
    X['pca-two'] = pca_result[:,1] 
    X['pca-three'] = pca_result[:,2]
    
    return X, pca_result


# print with PCA in 2D
def print_PCA_2D(X, table, target):
    plt.figure(figsize=(16,10))
    title = get_title("PCA 2D", table, target)
    plt.title(title)
    sns.scatterplot(
        x="pca-one", y="pca-two",
        palette=sns.color_palette("hls", 10),
        data=X,
        legend="full",
        alpha=0.3
    )


# print with PCA in 3D
def print_PCA_3D(X, Y, table, target):
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
    title = get_title("PCA 3D", table, target)
    plt.title(title)
    plt.show()


# print with t-SNE
def print_t_SNE(X, pca_result, table, target):
    tsne = TSNE(n_components=2, verbose=0, perplexity=40, n_iter=300)
    tsne_pca_results = tsne.fit_transform(pca_result)

    X['tsne-one'] = tsne_pca_results[:,0]
    X['tsne-two'] = tsne_pca_results[:,1]
    
    plt.figure()
    title = get_title("t-SNE", table, target)
    plt.title(title)
    sns.scatterplot(
        x="tsne-one", y="tsne-two",
        palette=sns.color_palette("hls", 10),
        data=X,
        legend="full",
        alpha=0.3,
    )
    