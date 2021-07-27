#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import numpy as np
from PIL import  Image
def app():
    #display = Image.open('113495828-rental-bikes-in-seoul-south-korea-use-app-and-rent-price-is-very-cheap.jpg')
    #display = np.array(display)
    #st.title("Rental Share",)
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    
    st.markdown("<h1 style='text-align: center; color: black;'>Rental Bike Demand Prediction in Seoul</h1>", unsafe_allow_html=True)
    #st.markdown("<style> body {background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");background-size: cover;}</style>", unsafe_allow_html=True)
    #st.image(display, width = 800)
    
    col2,col3,col4 = st.beta_columns([1,5,1])


    
    with col2:
        st.write("")

    with col3:
        st.image("bike.png",width=500,caption="Rental bike demand")

    with col4:
        st.write("")
    
    st.markdown("<h6 style='text-align: center; color: black;'>Created By: Sartyaki || Pranav || Som Nath</h6>", unsafe_allow_html=True)


# In[ ]:




