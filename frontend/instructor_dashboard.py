import streamlit as st

def instructor_dashboard():
    st.title("Instructor Dashboard 👩‍🏫")
    st.markdown("### Assign Learning Path")
    st.selectbox("Choose Group", ["Group A", "Group B"])
    st.button("Assign")

    st.markdown("### Group Leaderboard")
    st.table({
        "Learner": ["Alice", "Bob"],
        "XP": [100, 50]
    })

