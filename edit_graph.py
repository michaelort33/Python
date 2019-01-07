#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:31:12 2019

@author: michael
"""

def convert_nodes_to_name(list_of_paths,node):
    main_list=[]
    for each_list in list_of_paths:
        new_list=[]
        for each_node in each_list:
           new_list.append(node[node.loc[:,'deID']==each_node]['Node'].to_string(index=False))
        main_list.append(new_list)
    return main_list

def individual_node_to_name(deID,node):
    return node[node['deID']==deID]['Node']

