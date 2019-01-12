# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import edit_graph as eg
import networkx as nx

#Read from data base
#remote
#engine = create_engine("mysql://gregen5_root:Mooose33@gregenome.com/gregen5_gre_questions")
#local
engine = create_engine("mysql://root:@127.0.0.1/gre_genome")
my_con=engine.connect()

node = pd.read_sql('SELECT * FROM node', con=my_con)
edge = pd.read_sql('SELECT * FROM edge', con=my_con)
#quiz = pd.read_sql('SELECT * FROM quiz', con=my_con)
#join_table = pd.read_sql('SELECT * FROM join_table', con=my_con)


#node.to_sql(con=engine, if_exists='replace', index=False, name='node')
#edge.to_sql(con=engine, if_exists='replace', index=False, name='edge')
#join_table.to_sql(con=engine, if_exists='replace', index=False, name='join_table')
#quiz.to_sql(con=engine, if_exists='replace', index=False, name='quiz')

#node.to_pickle("./node.pkl")
#edge.to_pickle("./edge.pkl")
#join_table.to_pickle("./join_table.pkl")
#quiz.to_pickle("./quiz.pkl")