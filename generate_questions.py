# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 22:00:12 2018

@author: micha
"""
from random import randint
import os
import pandas

#read names csv
os.chdir("C:/Users/micha/OneDrive/Business/GRE Genome/Categories")
names = pandas.read_csv("baby-names.csv")

#generate new numbers for word problem algebraic translation, system of two
# equations


pairs=(('tall','heights'),('old','ages'),('rich','money'),
       ('wise','wisdom-scores'))


#Function to generate random names
def get_rand_name(names=names,num_names=1):
    rand=[]
    for x in range(num_names):
        rand.append(randint(0,len(names.index)-1))
        
    rand_names=names.iloc[rand,1]
    return rand_names


def generate_rand_question_algebraic_translations_1(pairs,names=names):
    x= (randint(2, 5))
    z=randint(1,25)*(x+1)
    question_names=get_rand_name(names,num_names=2)
    rand_pair=randint(0,len(pairs)-1)
    my_rand_pair=pairs[rand_pair]
    which_rand_name=randint(0,len(question_names.values)-1)
    
    q1="""{name1} is {x} times as {adjective1} as {name2}.
If {name1} and {name2}'s {adjective2} add up to {z}, 
how {adjective1} is {name_1_2}?""".format(x=x,z=z,adjective1=
    my_rand_pair[0],adjective2=my_rand_pair[1],
    name1=question_names.values[0],name2=question_names.values[1],name_1_2=
    question_names.values[which_rand_name])
    print(q1)
    

#generate new numbers for scaling problems with compound scaling.
    
object_pairs=(('triangle','an','area','base','multiplied'))
variables=('x')

def generate_rand_question_compound_functions_1(object_pairs=object_pairs,
                                                variables=variables):
    x= (randint(1, 25))
    y=randint(1,25)
    rand=randint(0,len(variables)-1)
    q1="""A {obj} has {article} {main_object} of {x}. 
    If the {sub_object} of the {obj} is {operation} by {y}, 
    what is the {main_object} of the resulting {obj} in terms of {x}?
    """.format(obj=object_pairs[0],article=object_pairs[1],
    main_object=object_pairs[2],x=variables[rand],
    sub_object=object_pairs[3],operation=object_pairs[4],y=y)
    print(q1)

changes=('increased','decreased')
percent_pairs=(('investment'),(''))

def generate_rand_question_successive_percents_1(percent_pairs,changes): 
    percent1=randint(1,100)
    percent2=randint(1,100)
    names=get_rand_name(num_names=1)
    change1=changes[randint(0,len(changes)-1)]
    change2=changes[randint(0,len(changes)-1)]
    which_object_cat=randint(0,len(percent_pairs)-1)
    object_cat=percent_pairs[which_object_cat]
    
    q1="""In 2014, {name0} {verb0} his {noun0} in {noun1}. From 2014 to 2015, 
    his {object0} {change1} by {percent1}%. 
    From 2015 to 2016, his remaining money {change2} by {percent2}%. 
    At the start of 2016, how much money does {name0} have as 
    a percentage of his original investment.""" .format(object0=object_cat,percent1=percent1,
    percent2=percent2,name0=names.values[0],change1=change1,change2=change2)
    print(q1)
    
