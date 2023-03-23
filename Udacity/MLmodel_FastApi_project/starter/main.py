#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:59:31 2023

@author: adamelshimi
"""
import pandas as pd


filename = "./adult.data"

cols = ['age', 'workclass','fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country','salary']

data = pd.read_csv(filename, names=cols)

df = pd.DataFrame(data)

Y = df.pop('salary') 
X = df


# X_train
# x_val
# Y_train
# y_val


if __name__=="__main__":
    print(data.head())
    #print(data.describe())
    print(Y)
    print(X) 