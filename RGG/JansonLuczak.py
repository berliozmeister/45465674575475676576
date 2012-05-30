# -*- coding: utf-8 -*-
'''
Created on 24.05.2012

@author: berlioz

This is RGG v. 1.0.
@input: number of vertices, power of the model
@output: graph
'''

import numpy as np
import utils    
import networkx as nx
import random as rnd



# number of vertices
n = 10000

# create an empty graph on n vertices
G = nx.empty_graph(n)


# power of the model
beta = 1.7

# average degree of the graph
mean_degree = 50

# generate a power-law array with defined parameters
powerLawArray = utils.powerLawArray(n, beta, mean_degree)
print np.max(powerLawArray) #может просто последний элемент печатать? впрочем, неважно

# as stated in Chung-Lu article we create an array of ints just taking the lower bound of the values
# from the power-law sequence

#powerLawDegreeSequence = [0]*n
powerLawDegreeArray = np.array(powerLawArray, dtype = np.longlong)

print powerLawDegreeArray.size


# counter. sumOfDegrees = Sum_i d_i
sumOfDegrees = powerLawDegreeArray.sum()
print sumOfDegrees



# array of delimiters
delimiterArray = np.cumsum(powerLawDegreeArray)
delimiterArray = np.insert(delimiterArray, 0, 0) #adding 0 to the beginning
delimiterArray = np.delete(delimiterArray, n) # final edition of delimiterArray



#print delimiterArray[678]
#print delimiterArray[679]

a = 0
#нафига тут list и range? xrange OK.
for i in list(range(sumOfDegrees)):
    G.add_edge(np.searchsorted(delimiterArray, rnd.randrange(sumOfDegrees)),
               np.searchsorted(delimiterArray, rnd.randrange(sumOfDegrees)))
nx.write_adjlist(G, 'adj_matrix')



#defines number of vertex to which picked dot corresponds
print '\n'
#nx.write_adjlist(G, "file_adj")
#print delimiterArray[n-1]
#print np.searchsorted(delimiterArray, delimiterArray[n - 1] + 1)







