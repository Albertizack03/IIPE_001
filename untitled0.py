# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lDwnm9ZPEND51MLlbFLgJ9chMbGu8qj-
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

data_set=pd.read_csv('/content/insurance.csv')
le=LabelEncoder()
lr=LinearRegression()

rfr=RandomForestRegressor()


print(data_set.sample)

from sklearn.model_selection import train_test_split

label_mapping={
    'male':1,
    'female':0,
    'yes':1,
    'no':0,
    'southwest':0,
    'southeast':0.25,
    'northwest':0.5,
    'northeast':0.75
}
data_set['sex']=data_set['sex'].map(label_mapping)
data_set['smoker']=data_set['smoker'].map(label_mapping)
data_set.drop(['region'],axis=1,inplace=True)

print(data_set.describe)

#x=data_set(data_set.loc[:,data_set.columns != 'charges'])
x=data_set.iloc[:,0:5]
y=data_set.iloc[:,5]
# print(y)
# print(x)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.15)

lr.fit(x_train,y_train)

print(lr.score(x_test,y_test))
print(lr.coef_)

rfr.fit(x_train,y_train)
print(rfr.score(x_test,y_test))
#rfr.predict([[]])