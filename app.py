# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:27:40 2020

@author: Rahul
"""



import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("accident1.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def accident_predict(Start_Lat,Start_Long,Temperature,Wind_Chill,Humidity,Pressure,Visibility,Wind_Direction,Wind_Speed,Precipitation,Weather_con,Sunrise_Sunset):
    
    prediction=classifier.predict([[Start_Lat,Start_Long,Temperature,Wind_Chill,Humidity,Pressure,Visibility,Wind_Direction,Wind_Speed,Precipitation,Weather_con,Sunrise_Sunset]])
    print(prediction)
    return prediction
    
def main():
    st.title("Accident Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Accident Servity Prediction  </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Start_Lat = st.text_input("Start-Latitude",'Type Here')
    Start_Long = st.text_input("Start - longitude","Type Here")
    Temperature = st.text_input("Temperature","Type Here")
    Wind_Chill = st.text_input("Wind_Chill","Type Here")
    Humidity = st.text_input("Humidity","Type Here")
    Pressure = st.text_input("Presuure","Type Here")
    Visibility = st.text_input("Visibility","Type Here")
    Wind_Direction = st.text_input("Wind direction","Type Here")
    Wind_Speed = st.text_input("Wind_Speed","Type Here")
    Precipitation = st.text_input("Precipitation","Type Here")
    Weather_con = st.text_input("Weather Condition","Type Here")
    Sunrise_Sunset = st.text_input("Sunrise_Sunset","Type Here")
    result=""
    if st.button("Predict"):
        result=accident_predict(Start_Lat,Start_Long,Temperature,Wind_Chill,Humidity,Pressure,Visibility,Wind_Direction,Wind_Speed,Precipitation,Weather_con,Sunrise_Sunset)
        st.success('Accident Servity is - {}'.format(result))
        html_temp="""
        <ul>
        <li>Servity < 1 - <em>Less Dangerous</em></li>
        <li>Servity   1 - 2 <em>Caution Drive Safe<em></li>
        <li>Servity   2- 3  <em> Dont Travel </em> </li>
        </ul>
        
        """
        st.markdown(html_temp,unsafe_allow_html=True)
        
    if st.button("About"):
     
    
        st.text("Developed By Rahul")
        st.text("Built with Streamlit")
        
if __name__=='__main__':
    main()