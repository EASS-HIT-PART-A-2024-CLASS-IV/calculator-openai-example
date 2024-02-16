import streamlit as st
import requests

st.title('Addition App')

a = st.number_input('Enter first number', value=0)
b = st.number_input('Enter second number', value=0)

if st.button('Add'):
    response = requests.post('http://backend:8000/add', json={"a": a, "b": b})
    if response.status_code == 200:
        result = response.json()['result']
        st.success(f'The result is {result}')
    else:
        st.error('Error in calculation')

