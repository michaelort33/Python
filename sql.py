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

engine = create_engine("mysql://root:@127.0.0.1/gre_genome")
my_con=engine.connect()

node = pd.read_sql('SELECT * FROM node', con=my_con)
edge = pd.read_sql('SELECT * FROM edge', con=my_con)

node['GRE Question']=str(node['GRE Question'])

for row in range(len(node)-1):
    gre=node.loc[row,'GRE Question']
    gre=str(gre)
    if gre!='':
        node["QuestionNumber"]=node["QuestionNumber"].convert_objects(convert_numeric=True)
        node["deID"]=node["deID"].convert_objects(convert_numeric=True)
        magoosh_rows=node.iloc[[row]]
        magoosh_rows.loc['Node']='Magoosh'
        q_num=node['QuestionNumber'].max()+1
        magoosh_rows.loc['QuestionNumber']=q_num
        
        magoosh_rows.loc['GRE Question']=''
        
        magoosh_rows.loc['Path']='../QuestionPics/'+str(q_num)+'.png'

        
        deID=node['deID'].max()+1
        magoosh_rows.loc['deID']=deID
        
        node=node.append(magoosh_rows)
    
        
    
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
