#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
from PIL import  Image
def app():
    st.markdown("<h1 style='text-align: center; color: black;'>Dashboard Overview</h1>", unsafe_allow_html=True)
    
    html_temp="""
    <h4 style='text-align: center; color: black;'>For more understanding, please visit our 
    <a href="https://app.powerbi.com/view?r=eyJrIjoiYWQ2YzZkODAtNWRmZC00Y2U1LWE0MzUtMDA1ZjFmODRkNjFmIiwidCI6IjFmNDM2ODQxLWZkMzEtNGFhYy1iNDkyLTlkMWI2OTJjMTU3YiIsImMiOjEwfQ%3D%3D" style="color: blue; font-weight: bold;">PowerBI</a> dashboard file
    </h4>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    display = Image.open('dashboard.jpg')
    display = np.array(display)
    #st.title("Rental Share",)
    #st.markdown("<style> body {background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");background-size: cover;}</style>", unsafe_allow_html=True)
    st.image(display, width = 720)
    
    #col1, col2, col3 = st.beta_columns([1,6,1])

    #with col1:
     #   st.write("")

    #with col2:
    #    st.image("Rental_Bike.png",width=500)

    #with col3:
    #    st.write("")
    
   # st.markdown("<h6 style='text-align: center; color: white;'>Created By: Sartyaki || Pranav || Som Nath</h6>", unsafe_allow_html=True)


# In[ ]:




