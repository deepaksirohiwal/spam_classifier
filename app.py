import streamlit as st
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
import sklearn

ps=PorterStemmer()

#function for preprocessing the input data
def transform_text(text):
    text=text.lower()
    text= nltk.word_tokenize(text)
    #print(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    #making a clone of y
    text=y[:]
    y.clear() #clearing the content of the list and making it empty
    for i in text:
        #checking is the text havve any punctuation and stopwords
        if i not in stopwords.words('english') and string.punctuation:
            y.append(i)
    #stemming the text
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

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

