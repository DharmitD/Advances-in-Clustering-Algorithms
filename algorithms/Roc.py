from pyclustering.cluster.encoder import type_encoding;
import csv
from PIL import Image;
import numpy
from pyclustering.utils import euclidean_distance;
import pandas as  pd
import pyclustering.core.rock_wrapper as wrapper;
import matrix
from pyclustering.cluster import cluster_visualizer;
import timeit
import matplotlib.pyplot as plt
from pyclustering.cluster.rock import rock
class rock:

    def __init__(self, data, eps, number_clusters, threshold = 0.5, ccore = False):
        self.__pointer_data = data;
        self.__eps = eps;
        self.__number_clusters = number_clusters;
        self.__threshold = threshold;

        self.__clusters = None;

        self.__ccore = ccore;

        self.__degree_normalization = 1.0 + 2.0 * ( (1.0 - threshold) / (1.0 + threshold) );

        self.__adjacency_matrix = None;
        self.__create_adjacency_matrix;


    def process(self):
          if (self.__ccore is True):
            self.__clusters = wrapper.rock(self.__pointer_data, self.__eps, self.__number_clusters, self.__threshold);

          else:
            self.__clusters = [[index] for index in range(len(self.__pointer_data))];

            while (len(self.__clusters) > self.__number_clusters):
                indexes = self.__find_pair_clusters(self.__clusters);

                if (indexes != [-1, -1]):
                    self.__clusters[indexes[0]] += self.__clusters[indexes[1]];
                    self.__clusters.pop(indexes[1]);   # remove merged cluster.
                else:
                    break;  # totally separated clusters have been allocated


    def get_clusters(self):
         return self.__clusters;

    def get_cluster_encoding(self):
        return type_encoding.CLUSTER_INDEX_LIST_SEPARATION;


    def __find_pair_clusters(self, clusters):#Check if link is good
        maximum_goodness = 0.0;
        cluster_indexes = [-1, -1];

        for i in range(0, len(clusters)):
            for j in range(i + 1, len(clusters)):
                goodness = self.__calculate_goodness(clusters[i], clusters[j]);
                if (goodness > maximum_goodness):
                    maximum_goodness = goodness;
                    cluster_indexes = [i, j];

        return cluster_indexes;


    def __calculate_links(self, cluster1, cluster2):
        number_links = 0;

        for index1 in cluster1:#Call adjacency matrix and create link
            for index2 in cluster2:
                number_links += self.__adjacency_matrix[index1][index2];

        return number_links;


    def __create_adjacency_matrix(self):
        size_data = len(self.__pointer_data);

        self.__adjacency_matrix = [ [ 0 for i in range(size_data) ] for j in range(size_data) ];
        for i in range(0, size_data):
            for j in range(i + 1, size_data):
                distance = euclidean_distance(self.__pointer_data[i], self.__pointer_data[j]);
                if (distance <= self.__eps):
                    self.__adjacency_matrix[i][j] = 1;
                    self.__adjacency_matrix[j][i] = 1;



    def __calculate_goodness(self, cluster1, cluster2):#check goodness of the link
         number_links = self.__calculate_links(cluster1, cluster2);
         devider = (len(cluster1) + len(cluster2)) ** self.__degree_normalization - len(cluster1) ** self.__degree_normalization - len(cluster2) ** self.__degree_normalization;
         return (number_links / devider);

# Read sample for clustering from some file
def rocAlgo(filename,col_name):
    df=pd.read_csv(filename, usecols=[col_name])
    df[col_name] = df[col_name]
    rock_instance = rock (col_name,1.0,100)
       # Run cluster analysis
    rock_instance.process();
       # Obtain results of clustering
    clusters = rock_instance.get_clusters();
    print(clusters)
    print(timeit.timeit('"-".join(str(n) for n in range(100))',number=10000))
    #Visualize clusters:
    visualizer = cluster_visualizer();
    visualizer.append_clusters(clusters,col_name);
    visualizer.show(display=False)
    plt.savefig("C:/Users/Nupura Hajare/Desktop/flask_app/web/static/img/Roc.png")
