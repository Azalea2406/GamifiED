import streamlit as st
from Authentication.login_page import login_page
from ui.dashboard_page import learner_dashboard
from ui.instructor_page import instructor_dashboard

# Set page config
st.set_page_config(page_title="GamifiED", layout="wide")

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["user"] = {}

# Title & Logo
st.markdown("""
    <h1 style='text-align: center;'>🎮 GamifiED Learning Platform</h1>
    <hr>
""", unsafe_allow_html=True)

# Login / Signup flow
if not st.session_state["authenticated"]:
    login_page()

# Role-based dashboard
else:
    user = st.session_state.user
    role = user.get("role")

    with st.sidebar:
        st.title("GamifiED")
        st.markdown("## 📋 Navigation")

        st.markdown("---")
        st.write(f"👤 Logged in as: `{user.get('email')}`")
        st.write(f"🧑‍💼 Role: `{role}`")
        st.markdown("---")

        if st.button("Logout"):
            st.session_state["authenticated"] = False
            st.session_state["user"] = {}
            st.rerun()

    if role == "Learner":
        learner_dashboard(user)
    elif role == "Instructor":
        instructor_dashboard()
    else:
        st.error("Unknown role. Please re-login or contact support.")
