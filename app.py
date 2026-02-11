import streamlit as st
import pickle

st.title("Email Spam and Ham Classifier")
st.image("https://raw.githubusercontent.com/deepankarkotnala/Email-Spam-Ham-Classifier-NLP/master/images/email_spam_ham.png")

with open(r"model.pkl","rb") as file:
    Model=pickle.load(file)

text=st.text_input("Enter the mail:")

if st.button("Predict"):
    result=Model.predict([text])[0]

    if result=="spam":
        st.write("This is a Spam Mail")
        st.image("https://blogs.mtu.edu/it/files/2024/05/spam.png")
    else:
        st.write("This is a Ham Mail")
        st.image("https://media.istockphoto.com/id/2184116209/vector/3d-closed-mail-envelope-with-plane-icon.jpg?s=612x612&w=0&k=20&c=m4I3u-GpmlRXn8p6dKHJGsti5PiKEqSOxO09zcqjKz0=")