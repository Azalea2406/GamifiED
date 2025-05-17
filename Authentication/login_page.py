import streamlit as st
from backend import auth

def login_page():
    st.title("🔐 GamifiED Login")

    choice = st.radio("Choose an action:", ["Login", "Sign Up"])

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    #sign up code
    if choice == "Sign Up":
        confirm_password = st.text_input("Confirm Password", type="password")
        role = st.selectbox("I am a:", ["Learner", "Instructor"])
        username = st.text_input("Choose a Username")

        if st.button("Create Account"):
            if password != confirm_password:
                st.error("Passwords do not match!")
            elif email and password and username:
                result = auth.signup_user(email, password, role.lower(), username)
                if result["success"]:
                    st.success("Account created! Please log in.")
                else:
                    st.error(f"Error: {result['error']}")
            else:
                st.warning("Please fill all fields.")
    # Login code 
    else:  
        if st.button("Login"):
            if email and password:
                result = auth.login_user(email, password)
                if result["success"]:
                    st.success(f"Welcome back, {result['user']['username']}!")
                    st.session_state["user"] = result["user"]
                else:
                    if "EMAIL_NOT_FOUND" in result["error"]:
                        st.warning("Email not registered. Please sign up.")
                    elif "INVALID_PASSWORD" in result["error"]:
                        st.error("Incorrect password. Try again or reset.")
                    else:
                        st.error(result["error"])