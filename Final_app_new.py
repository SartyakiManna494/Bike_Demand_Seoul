#!/usr/bin/env python
# coding: utf-8

# In[2]:



import streamlit as st
from multiapp import MultiApp
import Home, Predictor,Dashboard,Background # import your app modules here

Final = MultiApp()

# Add all your application here
Final.add_app("Home", Home.app)
#Final.add_app("Overview", Overview.app)
Final.add_app("Dashboard", Dashboard.app)
Final.add_app("Background", Background.app)
Final.add_app("Predictor", Predictor.main)

# The main app
Final.run()


# In[ ]:




