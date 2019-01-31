"""
Spyder Editor

This is a temporary script file.
"""
#%%
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import edit_graph as eg
import networkx as nx
from collections import Counter
import os


#%%Read from data base
os.chdir('/home/michael/GREGenome/Python')

#remote
remote_engine = create_engine("mysql+pymysql://gregen5_root:Mooose33@gregenome.com/gregen5_gre_questions")
my_con_remote=remote_engine.connect()

#local
local_engine = create_engine("mysql+pymysql://root:@127.0.0.1/gre_genome")
my_con_local=local_engine.connect()


node = pd.read_sql('SELECT * FROM node', con=local_engine)
edge = pd.read_sql('SELECT * FROM edge', con=local_engine)
quiz = pd.read_sql('SELECT * FROM quiz', con=local_engine)
join_table = pd.read_sql('SELECT * FROM join_table', con=local_engine)
users = pd.read_sql('SELECT * FROM users', con=local_engine)


#Write
#node.to_sql(con=local_engine, if_exists='replace', index=False, name='node')
#edge.to_sql(con=local_engine, if_exists='replace', index=False, name='edge')
#join_table.to_sql(con=local_engine, if_exists='replace', index=False, name='join_table')
#quiz.to_sql(con=local_engine, if_exists='replace', index=False, name='quiz')
#users.to_sql(con=local_engine, if_exists='replace', index=False, name='users')

#pickle
#node.to_pickle("./node.pkl")
#edge.to_pickle("./edge.pkl")
#join_table.to_pickle("./join_table.pkl")
#quiz.to_pickle("./quiz.pkl")
#users.to_pickle("./users.pkl")

#node = pd.read_pickle("./node.pkl")
#edge = pd.read_pickle("./edge.pkl")
#quiz = pd.read_pickle("./quiz.pkl")
#join_table = pd.read_pickle("./join_table.pkl")
#users = pd.read_pickle("./users.pkl")

#analyze which magoosh i have already: