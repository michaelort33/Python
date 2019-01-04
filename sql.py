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

node = pd.read_sql('SELECT * FROM node_backup', con=my_con)
edge = pd.read_sql('SELECT * FROM edge_backup', con=my_con)

#Set path to 0 when there is no picture
node['Path']=np.where(node['Has pic']=='0','',node['Path'])

node["QuestionNumber"]=node["QuestionNumber"].convert_objects(convert_numeric=True)
node["deID"]=node["deID"].convert_objects(convert_numeric=True)

to_do=node['GRE Question'].unique()

##########
node.loc[-1]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'5566','','','','','','','')

node[node['GRE Question']=='5566']['deID'].as_matrix()

edge[edge['End Vertex']==340]
edge[edge['End Vertex']==388]
edge[edge['End Vertex']==399]
edge[edge['End Vertex']==671]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,88,node['deID'].max())
edge.loc[len(edge)+1]=(geID,248,node['deID'].max())
edge.loc[len(edge)+1]=(geID,314,node['deID'].max())
edge.loc[len(edge)+1]=(geID,231,node['deID'].max())


#################
node.loc[-2]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'107','','','','','','','')

node[node['GRE Question']=='107']['deID'].as_matrix()

edge[edge['End Vertex']==343]
edge[edge['End Vertex']==400]
edge[edge['End Vertex']==402]
edge[edge['End Vertex']==403]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,88,node['deID'].max())
edge.loc[len(edge)+1]=(geID,314,node['deID'].max())
edge.loc[len(edge)+1]=(geID,315,node['deID'].max())

###############

node.loc[-3]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'2184','','','','','','','')

node[node['GRE Question']=='2184']['deID'].as_matrix()

edge[edge['End Vertex']==345]
edge[edge['End Vertex']==365]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,88,node['deID'].max())
edge.loc[len(edge)+1]=(geID,92,node['deID'].max())

#############

node.loc[-4]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'144','','','','','','','')

node[node['GRE Question']=='144']['deID'].as_matrix()

edge[edge['End Vertex']==346]
edge[edge['End Vertex']==368]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,88,node['deID'].max())
edge.loc[len(edge)+1]=(geID,94,node['deID'].max())

##########

node.loc[-5]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'6148','','','','','','','')

node[node['GRE Question']=='6148']['deID'].as_matrix()

edge[edge['End Vertex']==347]
edge[edge['End Vertex']==544]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,88,node['deID'].max())
edge.loc[len(edge)+1]=(geID,288,node['deID'].max())

#######

node.loc[-6]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'113','','','','','','','')

node[node['GRE Question']=='113']['deID'].as_matrix()

edge[edge['End Vertex']==349]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,242,node['deID'].max())

#####
node.loc[-7]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'338','','','','','','','')

node[node['GRE Question']=='338']['deID'].as_matrix()

edge[edge['End Vertex']==355]
edge[edge['End Vertex']==586]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,89,node['deID'].max())
edge.loc[len(edge)+1]=(geID,295,node['deID'].max())
edge.loc[len(edge)+1]=(geID,21,node['deID'].max())

###
node.loc[-8]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'154','','','','','','','')

node[node['GRE Question']=='154']['deID'].as_matrix()

edge[edge['End Vertex']==356]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,89,node['deID'].max())

#####

node.loc[-9]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'119','','','','','','','')

node[node['GRE Question']=='119']['deID'].as_matrix()

edge[edge['End Vertex']==358]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,89,node['deID'].max())

#########

node.loc[-10]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'122','','','','','','','')

node[node['GRE Question']=='122']['deID'].as_matrix()

edge[edge['End Vertex']==359]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,89,node['deID'].max())

##########

node.loc[-11]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'79','','','','','','','')

node[node['GRE Question']=='79']['deID'].as_matrix()

edge[edge['End Vertex']==362]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,90,node['deID'].max())

###

node.loc[-12]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'5583','','','','','','','')

node[node['GRE Question']=='5583']['deID'].as_matrix()

edge[edge['End Vertex']==366]
edge[edge['End Vertex']==367]
edge[edge['End Vertex']==375]
edge[edge['End Vertex']==401]
edge[edge['End Vertex']==404]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,93,node['deID'].max())
edge.loc[len(edge)+1]=(geID,94,node['deID'].max())
edge.loc[len(edge)+1]=(geID,243,node['deID'].max())
edge.loc[len(edge)+1]=(geID,314,node['deID'].max())
edge.loc[len(edge)+1]=(geID,328,node['deID'].max())


############
node.loc[-13]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'12633','','','','','','','')

node[node['GRE Question']=='12633']['deID'].as_matrix()

edge[edge['End Vertex']==374]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,244,node['deID'].max())

#######

node.loc[-14]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'5998','','','','','','','')

node[node['GRE Question']=='5998']['deID'].as_matrix()

edge[edge['End Vertex']==387]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,247,node['deID'].max())

#######

node.loc[-15]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'108','','','','','','','')

node[node['GRE Question']=='108']['deID'].as_matrix()

edge[edge['End Vertex']==413]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,255,node['deID'].max())


#######

node[node['GRE Question']=='4734']['deID'].as_matrix()

edge[edge['End Vertex']==427]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,257,470)

#######

node.loc[-16]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'12651','','','','','','','')

node[node['GRE Question']=='12651']['deID'].as_matrix()

edge[edge['End Vertex']==428]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,257,node['deID'].max())

#######

node.loc[-17]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'5999','','','','','','','')

node[node['GRE Question']=='5999']['deID'].as_matrix()

edge[edge['End Vertex']==444]

geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,317,node['deID'].max())

#######

node.loc[-18]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'14','','','','','','','')

node[node['GRE Question']=='14']['deID'].as_matrix()

edge[edge['End Vertex']==503]
edge[edge['End Vertex']==590]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,148,node['deID'].max())
edge.loc[len(edge)+1]=(geID,154,node['deID'].max())
edge.loc[len(edge)+1]=(geID,110,node['deID'].max())
edge.loc[len(edge)+1]=(geID,21,node['deID'].max())


#######

node.loc[-19]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'12636','','','','','','','')

node[node['GRE Question']=='12636']['deID'].as_matrix()

edge[edge['End Vertex']==504]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,148,node['deID'].max())
edge.loc[len(edge)+1]=(geID,154,node['deID'].max())

#######

node.loc[-20]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'12671','','','','','','','')

node[node['GRE Question']=='12671']['deID'].as_matrix()

edge[edge['End Vertex']==574]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,200,node['deID'].max())

#######

node.loc[-21]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'12581','','','','','','','')

node[node['GRE Question']=='12581']['deID'].as_matrix()

edge[edge['End Vertex']==575]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,200,node['deID'].max())

#######

node.loc[-22]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'12670','','','','','','','')

node[node['GRE Question']=='12670']['deID'].as_matrix()

edge[edge['End Vertex']==583]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,21,node['deID'].max())

#######

node.loc[-23]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'325','','','','','','','')

node[node['GRE Question']=='325']['deID'].as_matrix()

edge[edge['End Vertex']==585]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,21,node['deID'].max())
edge.loc[len(edge)+1]=(geID,88,node['deID'].max())


#######

node.loc[-24]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'182','','','','','','','')

node[node['GRE Question']=='182']['deID'].as_matrix()

edge[edge['End Vertex']==587]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,21,node['deID'].max())


#######

node.loc[-25]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'797','','','','','','','')

node[node['GRE Question']=='797']['deID'].as_matrix()

edge[edge['End Vertex']==596]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,22,node['deID'].max())

#######

node.loc[-26]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'838','','','','','','','')

node[node['GRE Question']=='838']['deID'].as_matrix()

edge[edge['End Vertex']==651]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,331,node['deID'].max())

#######

node.loc[-27]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'857','','','','','','','')

node[node['GRE Question']=='857']['deID'].as_matrix()

edge[edge['End Vertex']==653]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,325,node['deID'].max())

#######
node[node['GRE Question']=='6016']['deID'].as_matrix()

edge[edge['End Vertex']==658]
edge[edge['End Vertex']==676]



geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,332,676)

#######

node.loc[-28]=(node['deID'].max()+1,'Magoosh',
        '../QuestionPics/'+str(node['QuestionNumber'].max()+1)+'.png',1,
        node['QuestionNumber'].max()+1,'6021','','','','','','','')

node[node['GRE Question']=='6021']['deID'].as_matrix()

edge[edge['End Vertex']==672]


geID=edge['geID'].max()+1

edge.loc[len(edge)+1]=(geID,231,node['deID'].max())

############

node.loc[node.loc[:,'Node']=='Magoosh','Path']='../QuestionPics/Q'+round(node.loc[node.loc[:,'Node']=='Magoosh','QuestionNumber'],0).astype(int).astype(str)+'.png'

##########



#node.to_sql(con=engine, if_exists='replace', index=False, name='node')
#edge.to_sql(con=engine, if_exists='replace', index=False, name='edge')


