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
import edit_graph as eg
import json
from collections import Counter


###
#Create graph with networkx. This is one of tow graphs. The first with network
#x and that is called G (caps) The second is just for drawing and that is called 
#g (lowercase)

G = nx.DiGraph()

graph_edges=edge[['Start Vertex','End Vertex']]
tuple_edges=[tuple(x) for x in graph_edges.values]
               
graph_nodes=node[['deID']]
tuple_nodes=list(graph_nodes.values)
#Flatten the list of lists above
tuple_nodes=[item for sublist in tuple_nodes for item in sublist]

G.add_nodes_from(tuple_nodes)
G.add_edges_from(tuple_edges)

# Generate json for d3.js
def mapping(x):
    return str(x)

string_G=nx.relabel_nodes(G,mapping)

#nx to generate dictionary
d3_graph=nx.node_link_data(string_G)

#serialize dictionary with json and save it to file
with open('d3_graph_json.txt', 'w') as f:
    json.dump(d3_graph,f, ensure_ascii=False)
    
##generate svg or pdf with g.

g=Digraph(filename='gre_genome.gv',format='svg',graph_attr={"rankdir":"LR"})

#Define all nodes that are questions

QuestionNodes = list(node['deID'][node['QuestionNumber'].isin([x for x in node['QuestionNumber'] if x is not None])])

#Change all nodes to names but for the questions (The question names cause an error in g.render)

graph_edges['Start Vertex']=eg.convert_nodes_to_name([list(graph_edges['Start Vertex'])],node)[0]
graph_edges['End Vertex'][~graph_edges['End Vertex'].isin(QuestionNodes)]=eg.convert_nodes_to_name([list(graph_edges['End Vertex'][~graph_edges['End Vertex'].isin(QuestionNodes)])],node)[0]

graph_nodes['deID'][~graph_nodes['deID'].isin(QuestionNodes)]=eg.convert_nodes_to_name([list(graph_nodes['deID'][~graph_nodes['deID'].isin(QuestionNodes)])],node)[0]

#Add edges to the graph from graphviz
list_edges=[list(x) for x in graph_edges.values]

for x in list_edges:
    g.edge(str(x[0]),str(x[1]))
    
list_nodes=[list(x) for x in graph_nodes.values]
#set the link by first testing if the node is a question or not. if question link to question if 
#node link to quiz on that category
for x in list_nodes:
    if x[0] in QuestionNodes:
        URL=str('../PHP/questions_cat.php?question=('+'&quot;'+str(x[0])+'&quot;'+')')
    else:
        URL=str('../PHP/questions_cat.php?nodes=('+'&quot;'+str(x[0])+'&quot;'+')')
    g.node(name=str(x[0]),URL=URL,_attributes={"fontcolor":"red","target":"_blank","fillcolor":"lightgrey","style":"radial"})

#render the graphviz graph
g.render('../Website/QuestionPics/gre_genome')

###

#I will get all root and leaf nodes so i can get all paths from root to leaf

leaf_nodes = [node for node in G if len(list(G.neighbors(node)))==0]

root_nodes = list(set(edge['Start Vertex']
                [~edge.loc[:,'Start Vertex'].isin(edge.loc[:,'End Vertex'])]))

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

