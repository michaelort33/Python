# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sqlalchemy import create_engine
import MySQLdb
import mysql.connector
import pandas as pd
import numpy as np

engine = create_engine("mysql://root:Mooose33@127.0.0.1/gre_genome")
my_con=engine.connect()

node = pd.read_sql('SELECT * FROM node', con=my_con)
edge = pd.read_sql('SELECT * FROM edge', con=my_con)

node["QuestionNumber"]=node["QuestionNumber"].convert_objects(convert_numeric=True)

def transfer_magoosh(qid,node,edge):
    magoosh_rows=node.loc[node['GRE Question']==qid]
    magoosh_rows=magoosh_rows.copy()

    for x in range(len(magoosh_rows)):
        magoosh_rows['QuestionNumber'][x]=node['QuestionNumber'].max()+1+x
        magoosh_rows['Node'][x]='Magoosh'
        
        q_num=node['QuestionNumber'].max()+1+x
        q_num=str(q_num)
        magoosh_rows['Path'][x]='../QuestionPics/'+q_num+'.png'
        
        magoosh_rows['GRE Question'][x]=''
        
        magoosh_rows['QuestionNumber'][x]=q_num
        
        deID=node['deID'].max()+1+x
        
        magoosh_rows['deID'][x]=deID
        
        return magoosh_rows
    
    #multiple
    current_deID=node['deID'][node['GRE Question']==qid]
    start_nodes=edge['Start Vertex'][edge['End Vertex']==current_deID]
    new_edge_index=len(edge)+1
    geID=edge['geID'].max()+1
    edge.loc[new_edge_index]=(geID,88,current_deID)
node.at[338,"GRE Question"]=""



node.loc[552]=('788','Magoosh',
                   '../QuestionPics/Q214.png',1,214,'','','','','','','','')
edge.loc[472]=(472,88,343)
node.at[341,"GRE Question"]=""

#Set path to 0 when there is no picture
node['Path']=np.where(node['Has pic']=='0','',node['Path'])

node.to_sql(con=engine, if_exists='replace', index=False, name='node_python')
