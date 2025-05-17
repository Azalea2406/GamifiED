import streamlit as st
import plotly.express as px

def learner_dashboard():
    st.title("Welcome Learner 🎓")
    username = "JohnDoe"  # Replace with actual Firebase username fetch
    xp = 75

    st.subheader(f"Username: {username}")
    st.write(f"Total XP: {xp}")

    st.markdown("### Badges")
    st.image("https://img.icons8.com/color/96/medal.png", width=50)

    st.markdown("### Learning Path")
    st.progress(xp / 100)

    if st.button("Start Quiz"):
        st.info("Load MCQs here...")

    st.markdown("### Leaderboard (Sample)")
    st.table({
        "Name": ["John", "Jane", "Bob"],
        "XP": [75, 50, 25]
    })

