import streamlit as st
import sklearn
import joblib
model = joblib.load('SentimentAnalysis_model')
st.title('Sentiment Analysis Classifier')
ip = st.text_input("Enter the message")
op = model.predict([ip])
if st.button('Sentiment'):
  st.title(op[0])   
