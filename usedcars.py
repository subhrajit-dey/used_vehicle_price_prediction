# Data analytics on old car price prediction

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import pickle


#Read the data
cars = pd.read_csv('data_train (1).csv')
cars_copy = cars.copy()
cars=cars.drop(['Unnamed: 0'],axis=1)
cars=cars.drop(['New_Price'],axis=1)


cars['Power(bhp)'] = cars['Power(bhp)'].fillna(cars['Power(bhp)'].median())
cars['Seats'] = cars['Seats'].fillna(cars['Seats'].median())


data_to_scale = ['Year','Kilometers_Driven','Mileage(km/kg)','Engine(CC)','Power(bhp)'] #Extract the numerical columns


cars['Year'] = cars['Year'].astype('float64')
cars['Kilometers_Driven'] = cars['Kilometers_Driven'].astype('float64')
cars['Mileage(km/kg)'] = cars['Mileage(km/kg)'].astype('float64')
cars['Engine(CC)'] = cars['Engine(CC)'].astype('float64')
cars['Power(bhp)'] = cars['Power(bhp)'].astype('float64')



for i in range (0,len(cars['Year'])):
    if cars['Year'][i] < -3.5:
        cars['Year'][i] = -3.5


for i in range (0,len(cars['Kilometers_Driven'])):
    if cars['Kilometers_Driven'][i] > 1.5:
        cars['Kilometers_Driven'][i] = 1.5
        
for i in range (0,len(cars['Power(bhp)'])):
    if cars['Power(bhp)'][i] > 2.5:
        cars['Power(bhp)'][i] = 2.5

for i in range (0,len(cars['Engine(CC)'])):
    if cars['Engine(CC)'][i] > 3:
        cars['Engine(CC)'][i] = 3




categorical_cols = ['Location','Fuel_Type','Transmission','Owner_Type','Seats','Company']
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
cars[categorical_cols] = cars[categorical_cols].apply(lambda col: le.fit_transform(col))


cars['Power(bhp)'] = cars['Power(bhp)'].fillna(cars['Power(bhp)'].median())
cars['Mileage(km/kg)'] = cars['Mileage(km/kg)'].fillna(cars['Mileage(km/kg)'].median())
cars['Engine(CC)'] = cars['Engine(CC)'].fillna(cars['Engine(CC)'].median())
cars.dropna()

for col in cars.columns:
    print(col)




X = np.array(cars.drop(['Price'],axis = 1))
Y = np.array(cars[['Price']])


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.25, random_state = 1234)


#Linear Regression
from sklearn.linear_model import LinearRegression
std_reg = LinearRegression()
std_reg.fit(X_train,Y_train)

y_predict_std_reg = std_reg.predict(X_test)
score_std_reg = std_reg.score(X_test,Y_test)



pickle.dump(std_reg, open('uc.pkl', 'wb'))
