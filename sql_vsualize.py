# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import division
from sqlalchemy import create_engine
import pandas as pd
import networkx as nx
from graphviz import Digraph
import edit_graph




engine = create_engine("mysql://root:@127.0.0.1/gre_genome")
my_con=engine.connect()

node = pd.read_sql('SELECT * FROM node', con=my_con)
edge = pd.read_sql('SELECT * FROM edge', con=my_con)

###

G = nx.DiGraph()

graph_edges=edge[['Start Vertex','End Vertex']]
tuple_edges=[tuple(x) for x in graph_edges.values]

graph_nodes=node[['deID']]
tuple_nodes=[tuple(x) for x in graph_nodes.values]

G.add_edges_from(tuple_edges)
G.add_nodes_from(tuple_nodes)
    
##Draw

g=Digraph(filename='gre_genome.gv',format='pdf')

list_nodes=[list(x) for x in graph_nodes.values]

for x in list_nodes:
    x=str(x)
    g.node(x)
    
list_edges=[list(x) for x in graph_edges.values]

for x in list_edges:
    g.edge(str(x[0]),str(x[1]))
    
g.render('gre_genome',view=True)

###

#I will get all root and leaf nodes so i can get all paths from root to leaf

leaf_nodes = [node for node in G if G.degree(node)==1]

root_nodes = list(set(edge['Start Vertex']
                [~edge.loc[:,'Start Vertex'].isin(edge.loc[:,'End Vertex'])]))

#I get all paths from root to leaf
paths=[]
for leaf in leaf_nodes:
    for root in root_nodes:
        paths.append(list(nx.all_simple_paths(G,root,leaf)))
        
paths=[item for item in paths if len(item) > 0]
paths = [item for sublist in paths for item in sublist]

#Convert all paths from root to leaf from deID to names

gre_genome=convert_nodes_to_name(paths,node)

#First find the max lengths of sublists so i can no how many categories i need:

lengths=[]
for var in gre_genome:
    lengths.append(len(var))
    
num_headers=max(lengths)
    
#Conver list of lists where inner list is path of names to a dataframe like
#Like the original excel sheet. 

headers=[]
for header in range(num_headers):
    headers.append(header)
gre_genome=pd.DataFrame(gre_genome,columns=headers)

#Sort it alphabetically


#node.to_sql(con=engine, if_exists='replace', index=False, name='node')
#edge.to_sql(con=engine, if_exists='replace', index=False, name='edge')