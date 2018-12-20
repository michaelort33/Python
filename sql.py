# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import mysql.connector
import pandas as pd
import numpy as np

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="gre_genome"

)

node = pd.read_sql('SELECT * FROM node', con=mydb)
edge = pd.read_sql('SELECT * FROM edge', con=mydb)

node["QuestionNumber"]=node["QuestionNumber"].convert_objects(convert_numeric=True)

node.loc[551]=('787','Magoosh',
                   '../QuestionPics/Q213.png',1,213,'','','','','','','','')

edge.loc[471]=(472,88,340)

node.at[338,"GRE Question"]=""

node.loc[552]=('788','Magoosh',
                   '../QuestionPics/Q214.png',1,214,'','','','','','','','')

edge.loc[472]=(472,88,343)

node.at[341,"GRE Question"]=""