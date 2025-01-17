import streamlit as st
import helper
import pickle
model_path='C:\\Users\\sahil\\Desktop\\duplicate questions\\model (1).pkl'

with open(model_path, 'rb') as file:
    model = pickle.load(file)

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')

