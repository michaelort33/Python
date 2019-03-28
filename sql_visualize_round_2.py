from sql_read_write import node, edge

import networkx as nx
from networkx.readwrite import json_graph
import json
import matplotlib.pyplot as plt

subset = edge[['StartVertex', 'EndVertex']]
tuples = [tuple(x) for x in subset.values]


G = nx.DiGraph()
G.add_edges_from(tuples)


d = json_graph.node_link_data(G)

json.dump(d, open('force.json', 'w'))

#Visualize

pos = nx.kamada_kawai_layout(G)

nx.draw_networkx(G,pos,node_size=100,node_color="#3D9BE9",font_size=0,font_color="#00C8DC",edge_color="#00C8DC",arrowsize=3)

fig = plt.figure(figsize=(21, 21), dpi=100)


plt.savefig('cool.png',facecolor=fig.get_facecolor())

fig = plt.figure(figsize=(21, 21), dpi=100)

# simple graph

G_logo = nx.DiGraph()

simple = [('1', '2'), ('1', '3'), ('1', '4'), ('1','5'),('2', '3'), ('4', '3'), ('5', '4'), ('1','6'), ('6','3')]

G_logo.add_edges_from(simple)

d = json_graph.node_link_data(G_logo)

json.dump(d, open('force.json', 'w'))

##show it

nx.draw_shell(G_logo, node_size=300, node_color="black", font_size=0, font_color="black", edge_color="black", arrowsize=3, width=3)

fig.set_facecolor("#3D9BE9")

plt.savefig('cool.png',transparent=True)