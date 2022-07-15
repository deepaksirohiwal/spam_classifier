import streamlit as st
from nltk.stem.porter import PorterStemmer
import pickle


ps=PorterStemmer()

#function for preprocessing the input data

transform_text=pickle.load(open('transform_text.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")
input_sms=st.text_area("Enter the message")


if st.button('Predict'):
    transform_sms=transform_text(input_sms)

    prediction=model.predict([transform_sms])[0]

    if prediction==1:
        st.header("Spam")
    else:
        st.header("Not Spam")

