'''
Created on 29.05.2012

@author: berlioz
'''

import networkx as nx
import JansonLuczak as luc

nx.write_adjlist(luc.G, 'adj_matrix')