# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

engine = create_engine("mysql://root:@127.0.0.1/gre_genome")
my_con=engine.connect()

node = pd.read_sql('SELECT * FROM node', con=my_con)
edge = pd.read_sql('SELECT * FROM edge', con=my_con)

#node.to_sql(con=engine, if_exists='replace', index=False, name='node')
#node.to_sql(con=engine, if_exists='replace', index=False, name='edge')