# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:27:40 2020

@author: Rahul
"""

import numpy as np
import pandas as pd

df =pd.read_csv('Data1.csv')
df.head(5)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
# %matplotlib inline

st = pd.to_datetime(df.Start_Time, format='%d-%m-%Y %H:%M')
end = pd.to_datetime(df.End_Time, format='%d-%m-%Y %H:%M')

diff=(end-st)
nmore = diff.astype('timedelta64[m]').value_counts().nlargest(30)
nmore.plot.bar()

df['time'] = pd.to_datetime(df.Start_Time, format='%d-%m-%Y %H:%M')
df = df.set_index('time')
df.head()

def corr(df):
    df = df.dropna('columns') 
    df = df[[col for col in df if df[col].nunique() > 1]] 
    if df.shape[1] < 2:
        print('no use')
        return
    corr = df.corr()
    sns.heatmap(corr)
corr(df)

df_tem = df
df_tem.isnull().sum()

df_tem = df_tem.drop(['Distance(mi)', 'TMC', 'Country', 'Description', 'City', 'County', 'Street', 'Side', 'Zipcode', 'State', 'Airport_Code', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight'], axis=1)

cols = ["End_Lat", "End_Lng", "Number"]
df_tem = df_tem.drop(cols, axis=1)

pmean = df_tem['Pressure(in)'].mean()
tmean = df_tem['Temperature(F)'].mean()
wcmean = df_tem['Wind_Chill(F)'].mean()
hmean = df_tem['Humidity(%)'].mean()
wsmean = df_tem['Wind_Speed(mph)'].mean()
prmean = df_tem['Precipitation(in)'].mean()

df_tem['Pressure(in)']=df_tem['Pressure(in)'].fillna(pmean)
df_tem['Temperature(F)'] = df_tem['Temperature(F)'].fillna(tmean)
df_tem['Wind_Chill(F)'] = df_tem['Wind_Chill(F)'].fillna(wcmean)
df_tem['Humidity(%)'] = df_tem['Humidity(%)'].fillna(hmean)
df_tem['Wind_Speed(mph)'] = df_tem['Wind_Speed(mph)'].fillna(wsmean)
df_tem['Precipitation(in)']=df_tem['Precipitation(in)'].fillna(prmean)

visMode = df_tem["Visibility(mi)"].mode()
df_tem['Visibility(mi)'] = df_tem['Visibility(mi)'].fillna(df_tem['Visibility(mi)'].mode()[0])
df_tem['Wind_Direction'] = df_tem['Wind_Direction'].fillna(df_tem['Wind_Direction'].mode()[0])
df_tem['Weather_Condition'] = df_tem['Weather_Condition'].fillna(df_tem['Weather_Condition'].mode()[0])
df_tem['Sunrise_Sunset'] = df_tem['Sunrise_Sunset'].fillna(df_tem['Sunrise_Sunset'].mode()[0])

df_tem.dropna(axis=0, inplace=True)

df_tem.drop(['Timezone','Weather_Timestamp', 'Start_Time', 'End_Time', 'ID', 'Source',	'Amenity','Bump','Crossing',	'Give_Way',	'Junction',	'No_Exit',	'Railway'	,'Roundabout','Station',	'Stop','Traffic_Calming','Traffic_Signal','Turning_Loop'], axis = 1, inplace = True)

final_corr=df_tem.corr()
sns.heatmap(final_corr)

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
df_tem['Sunrise_Sunset'] = label_encoder.fit_transform(df_tem['Sunrise_Sunset'])
df_tem['Weather_Condition'] = label_encoder.fit_transform(df_tem['Weather_Condition'])
df_tem['Wind_Direction'] = label_encoder.fit_transform(df_tem['Wind_Direction'])

X = df_tem.drop(['Severity'], axis = 1)
Y = df_tem['Severity']

import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics

X_train, X_test, y_train, y_test = train_test_split(X, Y , test_size=0.2, random_state=120)

from sklearn.ensemble import RandomForestRegressor
regressor= RandomForestRegressor(n_estimators = 20,random_state=0)
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred.round()))



import pickle
pickle_out = open("accident.pkl","wb")
pickle.dump(regressor, pickle_out)
pickle_out.close()

