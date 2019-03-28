# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import division
import networkx as nx
from graphviz import Graph
import edit_graph as eg
from sql_read_write import *

import sys
from xml.dom import minidom
import simplejson

import os
###
#Create graph with networkx. This is one of tow graphs. The first with network
#x and that is called G (caps) The second is just for drawing and that is called 
#g (lowercase)

G = nx.DiGraph()

graph_edges=edge.loc[:,['StartVertex','EndVertex']]
tuple_edges=[tuple(x) for x in graph_edges.values]
               
graph_nodes=node.loc[:,['deID']]
tuple_nodes=list(graph_nodes.values)
#Flatten the list of lists above
tuple_nodes=[item for sublist in tuple_nodes for item in sublist]

#Add edges and nodes to networkx graph
G.add_nodes_from(tuple_nodes)
G.add_edges_from(tuple_edges)
    
##generate svg or pdf with g.

g=Graph(filename='gre_genome.gv',format='json',graph_attr={"rankdir":"LR"})

#Define all nodes that are questions

QuestionNodes = list(node.loc[:,'deID'][node['QuestionNumber'].isin([x for x in node['QuestionNumber'] if x is not None])])

#Change all nodes to names but for the questions (The question names cause an error in g.render)

#Everythin below until add edges is just changeing from nodes to Node names except for questions where i keep the 
#deID

graph_edges=graph_edges.reset_index(drop=True)

graph_edges=eg.convert_df_to_names(graph_edges,node,QuestionNodes)

graph_nodes=eg.convert_df_to_names(graph_nodes,node,QuestionNodes)

#Add edges to the graph from graphviz
list_edges=[list(x) for x in graph_edges.values]

for x in list_edges:
    g.edge(str(x[0]),str(x[1]))
    
list_nodes=[list(x) for x in graph_nodes.values]
    
#set the link by first testing if the node is a question or not. if question link to question if 
#node link to quiz on that category
for x in list_nodes:
    if x[0] in QuestionNodes:
        URL=str('../PHP/questions_cat.php?question='+str(x[0]))
    else:
        URL=str('../PHP/questions_cat.php?nodes='+str(x[0]))
    g.node(name=str(x[0]),URL=URL,_attributes={"fontcolor":"red","target":"_blank","fillcolor":"lightgrey","style":"radial"})

#render the graphviz graph
g.render('test')

###

#I will get all root and leaf nodes so i can get all paths from root to leaf

leaf_nodes = [node for node in G if len(list(G.neighbors(node)))==0]

root_nodes = list(set(edge['StartVertex']
                [~edge.loc[:,'StartVertex'].isin(edge.loc[:,'EndVertex'])]))

#Remove isolates from the gre_genome sheet
#root_nodes = [node for node in root_nodes if node not in nx.isolates(G)]

#I get all paths from root to leaf
paths=[]
for leaf in leaf_nodes:
    for root in root_nodes:
        paths.append(list(nx.all_simple_paths(G,root,leaf)))
        
paths = [item for item in paths if len(item) > 0]
paths = [item for sublist in paths for item in sublist]

#Convert all paths from root to leaf from deID to names

gre_genome=eg.df_from_paths(paths,node)

#Start analysis
analyze_isolates = node[node['deID'].isin(list(nx.isolates(G)))]

new_node=list(node.iloc[1])
new_edge=['',0,0]

