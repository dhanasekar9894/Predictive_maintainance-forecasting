# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:45:11 2024

@author: dhanasekar
"""

import pandas as pd
import numpy as np
import streamlit as st
import pickle

pickle_in = open('C:/Users/chandrasekar/Desktop/P_M_P/New folder/predictive_maintainance.sav','rb')

regressor = pickle.load(pickle_in)
pickle_in.close()

def predict_(mini,maxi,err,pixels):
    
    prediction=regressor.predict([[mini,maxi,err,pixels]])

    return prediction


def main():
    st.title("Predictive Maintainance")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Predictive Maintainance App for sensor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    mini = st.number_input("Minimum")
    maxi = st.number_input("Maximum")
    err = st.number_input("Error")
    pixels = st.number_input("Pixles")
    result=""
    if st.button("Predict"):
        result=predict_(mini,maxi,err,pixels)
        if err >= 12 :
            st.success('This sensor has been already failed since {} days'.format(round(result[0],0)))

        else:

            st.success('This will work till {} days'.format(round(result[0],0)))

    

if __name__=='__main__':
    main()