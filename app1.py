import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

pickle_in = open('rf.pkl', 'rb')
rf = pickle.load(pickle_in)

def welcome():
    return 'Welcome All'

def predict_rf(anaemia, diabetes,
       high_blood_pressure, sex, smoking, time): 
    prediction = rf.predict([[anaemia, diabetes, high_blood_pressure, sex, smoking, time]])
    print(prediction)
    return prediction

def main():
    st.title('Heart Failure Prediction')
    html_temp = '''
    <div style='background-color:tomato; padding:10px'>
    <h2 style='color:white; text-align:center'>Heart Failure Prediction ML App</h2>
    </div>
    <p>
    '''
    st.markdown(html_temp, unsafe_allow_html=True) 
    #age = st.text_input('Age', '...')
    anaemia = st.text_input('Anaemia (No = 0 ; Yes = 1)', '...')
    #creatinine_phosphokinase = st.text_input('Creatinine Phosphokinase', '...')
    diabetes = st.text_input('Diabetes (No = 0 ; Yes = 1)', '...')
    #ejection_fraction = st.text_input('Ejection Fraction',     '...')
    high_blood_pressure = st.text_input('High Blood Pressure (No = 0 ; Yes = 1)', '...')
    #platelets = st.text_input('Platelets', '...')
    #serum_creatinine = st.text_input('Serum Creatinine', '...')
    #serum_sodium = st.text_input('Serum Sodium', '...')
    sex = st.text_input('Sex (Female = 0 ; Male = 1)', '...')
    smoking = st.text_input('Smoking (No = 0 ; Yes = 1)', '...')
    time = st.text_input('Time (No = 0 ; Yes = 1)', '...')
    result=''
    if st.button('Predict'):
        result = predict_rf(anaemia, diabetes, high_blood_pressure, sex, smoking, time)
    st.success('The output is {}'.format(result))
    if st.button('About'):
        st.text('Lets Learn')
        st.text('Built with Streamlit')

if __name__=='__main__':
    main()
