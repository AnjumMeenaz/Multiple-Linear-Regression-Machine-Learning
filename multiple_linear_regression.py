# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 05:38:04 2019

@author: Admin
"""

# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

# Importing the dataset
dataset = pd.read_csv('E:\\MCA\\MCA 5th Sem\\Machine Learning\\ML Assigment\\Multiple-Linear-Regression-Machine-Learning\\50_Startups.csv')
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 4]

#Convert the column into categorical columns

states=pd.get_dummies(X['State'],drop_first=True)

# Drop the state coulmn
X=X.drop('State',axis=1)

# concat the dummy variables
X=pd.concat([X,states],axis=1)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

from sklearn.metrics import r2_score
score=r2_score(y_test,y_pred)

df = DataFrame(dataset,columns=['R&D Spend','Administration','Marketing','State','Profit'])
 
plt.scatter(df['Administration'], df['Profit'], color='red')
plt.title('Profit Vs Administration', fontsize=14)
plt.xlabel('Administration', fontsize=14)
plt.ylabel('Profit', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['R&D Spend'], df['Profit'], color='red')
plt.title('Profit Vs R&D Spend', fontsize=14)
plt.xlabel('R&D Spend', fontsize=14)
plt.ylabel('Profit', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['Marketing'], df['Profit'], color='red')
plt.title('Profit Vs Marketing', fontsize=14)
plt.xlabel('Marketing', fontsize=14)
plt.ylabel('Profit', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['State'], df['Profit'], color='red')
plt.title('Profit Vs State', fontsize=14)
plt.xlabel('State', fontsize=14)
plt.ylabel('Profit', fontsize=14)
plt.grid(True)
plt.show()
 