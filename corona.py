# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:42:58 2020

@author: 91905
"""
#importing libraries
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import numpy as np

#loading datasets
dataset=pd.read_csv('train.csv')
test_set=pd.read_csv('test.csv')
sub=pd.read_csv('submission.csv')
t=dataset.iloc[:,1:]
x=dataset.iloc[:,1:-1]
y=dataset.iloc[:,-1:]

province=pd.get_dummies(x['Province/State'])
x=pd.concat([x,province],axis=1)

country=pd.get_dummies(x['Country/Region'])
x=pd.concat([x,country],axis=1)
x.drop(["Country/Region"],axis=1)
x.drop(["Province/State"],axis=1)

#correlation check
#corr_matrix=t.corr()
#corr_matrix["ConfirmedCases"].sort_values(ascending=False)


