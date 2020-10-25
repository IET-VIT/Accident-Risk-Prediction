# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:27:40 2020

@author: Rahul

"""
# xnn



import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("accident.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def accident_predict(Start_Lat,Start_Long,Temperature,Wind_Chill,Humidity,Pressure,Visibility,Wind_Direction,Wind_Speed,Precipitation,Weather_con,Sunrise_Sunset):
    
    prediction=classifier.predict([[Start_Lat,Start_Long,Temperature,Wind_Chill,Humidity,Pressure,Visibility,Wind_Direction,Wind_Speed,Precipitation,Weather_con,Sunrise_Sunset]])
    print(prediction)
    return prediction
    
def main():
    st.title("@Travelify")
  
    html_temp = """
    <div style="background-color:Red;padding:10px">
    <h1 style="color:white;text-align:center;"><em>Accident Severity Prediction</em> </h1>
    </div>
    <br></br>
    """
    html_temp1='''
    <p>
    <a href="https://www.latlong.net/">To Get longitude and Latitude</a>
    </p>
    '''
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.markdown(html_temp1,unsafe_allow_html =True)
    st.write('''
    # Procedure to use this App:
    ### Input the following.
    * Get coordinates of your location using above link
    * Temperature 
    * Wind Chill - It is the lowering of body temperature due to the passing-flow of lower-temperature air.
    * Humidity , Pressure
    * Visibility 
    * Wind  Direction , Wind Speed
    * Precipitation
    * Weather Condition
    * Sunrise / Sunrise
''')
    Start_Lat = st.sidebar.slider("Start-Latitude",-90.0,90.0)
    Start_Long = st.sidebar.slider("Start - longitude",-180.0,180.0)
    Temperature = st.slider("Temperature(F)",32.0,212.0,1.0)
    x= (Temperature -32 )*5/9
    st.write("In celsius : {}".format(x))
    Wind_Chill = st.slider("Wind_Chill",-30.0,120.0,10.0)
    Humidity = st.number_input("Humidity(%)",0.0,100.0,step=5.0)
    Pressure = st.number_input("Pressure(in)",0.0,34.0,step=2.0)
    Visibility = st.number_input("Visibility",0.0,100.0,step=10.0)
    wd = ('Calm', 'SW', 'SSW', 'WSW', 'WNW', 'NW', 'West', 'NNW', 'NNE','South', 'North', 'Variable', 'SE', 'SSE', 'ESE', 'East', 'NE','ENE')
    options_wd = list(range(len(wd)))
    Wind_Direction = st.selectbox("Wind Direction", options_wd, format_func=lambda x: wd[x])
    Wind_Speed = st.slider("Wind_Speed(mph)",0.0,1000.0,50.0)
    Precipitation = st.slider("Precipitation(in)",0.0,11.0,0.3)
    wc=("Clear","Overcast","Mostly Cloudy","Partly Cloudy","Scattered Clouds","Light Rain","Haze","Light Snow","Fair","Rain","Fog","Heavy Rain")
    options_wc = list(range(len(wc)))
    Weather_con = st.selectbox("Weather Condition",options_wc,format_func=lambda x: wc[x])
    sun = ("Sunrise", "Sunset")
    options_sun = list(range(len(sun)))
    Sunrise_Sunset = st.selectbox("Sunrise/Sunrise", options_sun, format_func=lambda x: sun[x])
    result=""
    if st.button("Predict"):
        result=accident_predict(Start_Lat,Start_Long,Temperature,Wind_Chill,Humidity,Pressure,Visibility,Wind_Direction,Wind_Speed,Precipitation,Weather_con,Sunrise_Sunset)
        st.success('Accident Servity is - {}'.format(result))
        html_temp="""
        
        <ul>
        <li>Severity < 1 - <em>Less Dangerous</em></li>
        <li>Severity   1 - 2.5 <em>Caution Drive Safe<em></li>
        <li>Severity >  2.5  <em> Dont Travel </em> </li>
        </ul>
        </div>
        
        """
        st.markdown(html_temp,unsafe_allow_html=True)
        
    if st.button("About"):
     
    
        st.text("Developed By Rahul")
        st.text("Team Fourth Dimension")
        st.text("Future Update will make it realtime")
        
if __name__=='__main__':
    main()