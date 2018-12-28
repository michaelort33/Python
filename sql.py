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

node.loc[551]=('787','Magoosh',
                   '../QuestionPics/Q213.png',1,213,'','','','','','','','')

edge.loc[471]=(472,88,340)

node.at[338,"GRE Question"]=""

node.loc[552]=('788','Magoosh',
                   '../QuestionPics/Q214.png',1,214,'','','','','','','','')

edge.loc[472]=(472,88,343)

node.at[341,"GRE Question"]=""

node['Path']=np.where(node['Has pic']=='0','',node['Path'])

node.to_sql(con=engine, if_exists='replace', index=False, name='node_python')
