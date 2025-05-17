import streamlit as st
import pyrebase

firebaseConfig = {
    # paste your firebase config
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def login():
    st.title("Login Page")
    choice = st.selectbox("Login/Signup", ["Login", "Signup"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if choice == "Signup":
        if st.button("Create Account"):
            try:
                auth.create_user_with_email_and_password(email, password)
                st.success("Account created!")
            except:
                st.error("Email already exists or invalid password.")
    else:
        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.success("Logged in successfully!")
                st.session_state.user = user
            except:
                st.error("Incorrect credentials or user does not exist.")

