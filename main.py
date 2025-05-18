import streamlit as st
from Authentication.login_page import login_page
#from Authentication.auth import get_current_user
from ui.dashboard_page import learner_dashboard
from ui.instructor_page import instructor_dashboard

# Set page config
st.set_page_config(page_title="GamifiED", layout="wide")

# Session state for login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

# Title & Logo
st.markdown("""
    <h1 style='text-align: center;'>🎮 GamifiED Learning Platform</h1>
    <hr>
""", unsafe_allow_html=True)

# If not logged in, show login/signup
if not st.session_state.logged_in:
    login_page()

# If logged in, show dashboard based on role
else:
    user = st.session_state.user
    role = user.get("role", "learner")

    with st.sidebar:
        st.title("GamifiED")
        st.markdown("## 📋 Navigation")
        #show user profile info
        st.markdown("---")
        st.write(f"👤 Logged in as: `{user.get('username')}`")
        st.write(f"📧 Email: `{user.get('email')}`")
        st.write(f"🧑‍💼 Role: `{role}`")
        st.markdown("---")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.rerun()

    
    if role == "learner":
        learner_dashboard(user)
    elif role == "instructor":
        instructor_dashboard()
    else:
        st.error("Unknown role. Please contact support.")
