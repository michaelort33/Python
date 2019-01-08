#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:31:12 2019

@author: michael
"""
import pandas as pd

def convert_nodes_to_name(list_of_paths,node):
    main_list=[]
    for each_list in list_of_paths:
        new_list=[]
        for each_node in each_list:
           new_list.append(node[node.loc[:,'deID']==each_node]['Node'].to_string(index=False))
        main_list.append(new_list)
    return main_list

#Looks up deID and returns Node name
def individual_node_to_name(deID,node):
    return node[node['deID']==deID]['Node']


#Adds a new row to node or edge frame by changeging to list of lists appending a list
# and then changeing back :)
def add_new_rows(list_of_rows,df):
    names=df.columns.values
    df=df.values.tolist()
    for row in list_of_rows:
        df.append(row)
    df=pd.DataFrame(df)
    df.columns=names
    return df

