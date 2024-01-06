import streamlit as st 
import pickle

model=pickle.load(open('model.pkl','rb'))
st.title('salary exprience') 

AM=st.text_input('Enter the year:')


if st.button('Predict'):
    AM=float(AM) 
    

    data=[[AM]] 
    result=model.predict(data) 
    st.success(result)
