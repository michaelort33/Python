# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sqlalchemy import create_engine
import pandas as pd
import networkx as nx
import numpy as np



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

leaf_nodes = [node for node in G if G.degree(node)==1]

root_nodes = list(set(edge['Start Vertex']
                [~edge.loc[:,'Start Vertex'].isin(edge.loc[:,'End Vertex'])]))

paths=[]
for leaf in leaf_nodes:
    for root in root_nodes:
        paths.append(list(nx.all_simple_paths(G,root,leaf)))
        
paths=[item for item in paths if len(item) > 0]
paths = [item for sublist in paths for item in sublist]

            
def convert_node_to_name(list_of_paths,node):
    main_list=[]
    for each_list in list_of_paths:
        new_list=[]
        for each_node in each_list:
           new_list.append(node[node.loc[:,'deID']==each_node]['Node'].to_string(index=False,header=False))
        main_list.append(new_list)
    return main_list

test=convert_node_to_name(paths,node)
    
    

#node.to_sql(con=engine, if_exists='replace', index=False, name='node')
#edge.to_sql(con=engine, if_exists='replace', index=False, name='edge')