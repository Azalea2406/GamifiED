import streamlit as st
from firebase_config import db
from Quiz.quiz_engine import take_quiz
from Quiz.quiz_data import QUIZ_QUESTIONS
from Learning.course_data import COURSES
import pandas as pd
import altair as alt


def get_user_xp(user_id):
    progress = db.child("progress").child(user_id).get().val()
    total_xp = 0
    if progress:
        for course in progress.values():
            for level in course.values():
                total_xp += level.get("xp", 0)
    return total_xp


def get_xp_over_time(user_id):
    progress = db.child("progress").child(user_id).get().val()
    data = []

    if progress:
        for course, levels in progress.items():
            for level, details in levels.items():
                timestamp = details.get("timestamp") or "1970-01-01T00:00:00"
                xp = details.get("xp", 0)
                data.append({"Date": timestamp, "XP": xp, "Level": level})

    return pd.DataFrame(data)


def get_assigned_course(user_id):
    data = db.child("assignments").child(user_id).get().val()
    # Defensive: check data and key existence
    if data and isinstance(data, dict):
        return data.get("course")
    return None


def has_completed_level(user_id, course, level_index):
    path = f"progress/{user_id}/{course}/level_{level_index}"
    return db.child(path).get().val() is not None


def learner_dashboard(user):
    st.title("🎓 Learner Dashboard")

    # Try multiple ways to get user_id for robustness
    user_id = user.get("user_id") or user.get("localId") or st.session_state.get("user", {}).get("uid")
    username = user.get("username") or user.get("email") or "Learner"

    if not user_id:
        st.error("User ID not found. Please log in again.")
        return

    assigned_course = get_assigned_course(user_id)

    if not assigned_course:
        st.warning("No course assigned yet. Please wait for your instructor to assign one.")
        return

    st.subheader(f"📚 Assigned Course: {assigned_course}")

    total_xp = get_user_xp(user_id)
    st.success(f"🌟 Total XP: {total_xp}")

    # Profile Mock Section
    st.markdown("### 🧑 Learner Profile")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/1946/1946429.png", width=100)
    with col2:
        st.markdown(f"**Name:** {username}")
        st.markdown(f"**Course:** {assigned_course}")
        st.markdown(f"**Total XP:** {total_xp}")

    # XP Progress Chart
    xp_df = get_xp_over_time(user_id)
    if not xp_df.empty:
        st.markdown("### 📈 XP Progress Over Time")
        xp_df["Date"] = pd.to_datetime(xp_df["Date"], errors="coerce")
        xp_df = xp_df.sort_values("Date")

        chart = alt.Chart(xp_df).mark_line(point=True).encode(
            x="Date:T",
            y="XP:Q",
            tooltip=["Level", "XP", "Date"]
        ).properties(width=700, height=300)

        st.altair_chart(chart, use_container_width=True)

    st.markdown("---")
    st.subheader("📈 Progress & Quizzes")

    course = COURSES.get(assigned_course)
    if not course:
        st.error("Course data not found.")
        return

    for idx, level in enumerate(course["levels"]):
        level_name = level["name"]
        completed = has_completed_level(user_id, assigned_course, idx)

        with st.expander(f"Level {idx + 1}: {level_name} {'✅' if completed else ''}"):
            if completed:
                st.info("Level already completed.")
                continue

            questions = QUIZ_QUESTIONS.get(assigned_course, {}).get(level_name, [])
            if not questions:
                st.warning("No questions found for this level.")
                continue

            st.markdown("### 📝 Quiz Questions")
            answers = []
            all_answered = True

            for q_index, q in enumerate(questions):
                ans = st.radio(
                    f"{q_index + 1}. {q['question']}",
                    options=q['options'],
                    key=f"{level_name}_{q_index}"
                )
                answers.append(ans)
                if not ans:
                    all_answered = False

            if st.button(f"🚀 Submit Quiz - {level_name}", key=f"submit_{level_name}"):
                if not all_answered:
                    st.warning("⛔ Please answer all questions before submitting.")
                else:
                    with st.spinner("Submitting your quiz..."):
                        result = take_quiz(user_id, assigned_course, level_name, answers)
                        st.success(
                            f"✅ Submitted!\n\n🎯 Score: {result['score']}%\n🏆 XP Earned: {result['xp_result']['xp']}"
                        )
                        st.balloons()
                        st.rerun()

