'''
Created on 15 July, 2023

copyright--> Yashraj Singh Rajawat

'''


# importing libraries

import pandas as pd
import numpy as np
import streamlit as st
from pickle import dump
from pickle import load


st.title('Electric Motor Speed Prediction')



# creating a function for user inputs.
def main():
    u_q = st.number_input('Voltage D Component')
    u_d = st.number_input('Voltage Q Component')
    i_d = st.number_input('Current Q Component')
    pm = st.number_input('Permanent Magnent Temperature')
  
 # making a table of user inputs to process with model  
    data = {
        'u_q':u_q,
        'u_d':u_d,
        'i_d':i_d,
        'pm':pm
    }
    variables = pd.DataFrame(data,index=[0])
    return variables

st.subheader('Enter the Parameters')
loaded_model = load(open('adaboost.sav','rb'))


diagnosis = main()
st.write(diagnosis)
prediction = loaded_model.predict(diagnosis)
st.success(diagnosis)
# creating a button for Prediction
st.button('Result')
st.write('The motor speed for above inputs is ',prediction)
    
    



