#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pickle
#with open('Random_regression.pkl', 'rb') as file:
#    Pickled_LR_Model = pickle.load(file)
#Pickled_LR_Model


# In[2]:


import numpy as np
import pickle
import pandas as pd
import streamlit as st


# In[3]:


#!pip install streamlit


# In[4]:


pickle_in = open("Random_regression.pkl","rb")
resgressor = pickle.load(pickle_in)


# In[5]:


def predict_rental(Hour, Temperature, Humidity,
       Wind_speed, Visibility, Dew_point_temperature,
       Solar_Radiation, dayofWeek, Seasons,
       Holiday, Functioning_Day, Weather):
    if Seasons == 'Autumn':
        Seasons_Autumn = 1 
        Seasons_Spring = 0 
        Seasons_Summer = 0 
        Seasons_Winter = 0
    elif Seasons == 'Spring':
        Seasons_Autumn = 0 
        Seasons_Spring = 1 
        Seasons_Summer = 0 
        Seasons_Winter = 0
    elif Seasons == 'Summer':
        Seasons_Autumn = 0 
        Seasons_Spring = 0
        Seasons_Summer = 1 
        Seasons_Winter = 0
    else:
        Seasons_Autumn = 0
        Seasons_Spring = 0
        Seasons_Summer = 0
        Seasons_Winter = 1
        
    if Holiday == 'Yes':
        Holiday_No_Holiday = 0
    else:
        Holiday_No_Holiday = 1
        
    if Functioning_Day == 'Yes':
        Functioning_Day_No = 0
    else:
        Functioning_Day_No = 1
        
    if Weather == 'Weather_bad_weather':
        Weather_bad_weather =1
        Weather_clear_weather =0
        Weather_good_weather =0
        Weather_worst_weather =0
    elif Weather == 'Weather_clear_weather':
        Weather_bad_weather =0
        Weather_clear_weather =1
        Weather_good_weather =0
        Weather_worst_weather =0
    elif Weather == 'Weather_good_weather':
        Weather_bad_weather =0
        Weather_clear_weather =0
        Weather_good_weather =1
        Weather_worst_weather =0
    else:
        Weather_bad_weather =0
        Weather_clear_weather =0
        Weather_good_weather =0
        Weather_worst_weather =1
        
    
    prediction = resgressor.predict([[Hour, Temperature, Humidity,
       Wind_speed, Visibility, Dew_point_temperature,
       Solar_Radiation, dayofWeek, Seasons_Autumn,
       Seasons_Spring, Seasons_Summer, Seasons_Winter,
       Holiday_No_Holiday, Functioning_Day_No, Weather_bad_weather,
       Weather_clear_weather, Weather_good_weather,
       Weather_worst_weather]])
    prediction_n = np.round(np.exp(prediction)-1)
    print(prediction_n)
    return(prediction_n)


# In[6]:


def main():
    st.title("BIKE RENTAL PREDICTION")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit BIKE RENTAL PREDICTION APP </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    col1,col2 = st.beta_columns(2)
    with col1:
        Hour = st.text_input("Hour","Type Here")
        Humidity = st.text_input("Humidity(%)","Type Here")
        Temperature = st.text_input("Temperature(°C)","Type Here")
        Wind_speed = st.text_input("Wind speed (m/s)","Type Here")
        Visibility = st.text_input("Visibility (10m)","Type Here")
        Dew_point_temperature = st.text_input("Dew point temperature(°C)","Type Here")
    with col2:
        Solar_Radiation = st.text_input("Solar Radiation (MJ/m2)","Type Here")
        dayofWeek = st.text_input("dayofWeek","Type Here")
    #Seasons_Autumn = st.text_input("Seasons_Autumn","Type Here")
    #Seasons_Spring = st.text_input("Seasons_Spring","Type Here")
    #Seasons_Summer = st.text_input("Seasons_Summer","Type Here")
    #Seasons_Winter = st.text_input("Seasons_Winter","Type Here")
        Seasons = st.selectbox('Seasons', ('Autumn', 'Spring', 'Summer','Winter'))
        Holiday = st.selectbox('Holiday(Yes/No)',('Yes','No'))
        Functioning_Day = st.selectbox('Functioning_Day(Yes/No)',('Yes','No'))
        Weather = st.selectbox('Weather', ('Weather_bad_weather','Weather_clear_weather','Weather_good_weather','Weather_worst_weather'))
    #Holiday_No_Holiday = st.text_input("Holiday_No Holiday","Type Here")
    #Functioning_Day_No = st.text_input("Functioning Day_No","Type Here")
    #Weather_bad_weather = st.text_input("Weather_bad weather","Type Here")
    #Weather_clear_weather = st.text_input("Weather_clear weather","Type Here")
    #Weather_good_weather = st.text_input("Weather_good weather","Type Here")
    #Weather_worst_weather = st.text_input("Weather_worst weather","Type Here")
    result=""
    if st.button("Predict"):
        result = predict_rental(Hour, Temperature, Humidity,
       Wind_speed, Visibility, Dew_point_temperature,
       Solar_Radiation, dayofWeek, Seasons,
       Holiday, Functioning_Day, Weather)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets get value")
        st.text("Streamlit used")


# In[7]:


if __name__ =='__main__':
    main()


# In[ ]:




