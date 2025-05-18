import streamlit as st
from firebase_config import db
from Quiz.quiz_engine import take_quiz
from Quiz.quiz_data import QUIZ_QUESTIONS
from Learning.course_data import COURSES

def get_user_xp(user_id):
    progress = db.child("progress").child(user_id).get().val()
    total_xp = 0
    if progress:
        for course in progress.values():
            for level in course.values():
                total_xp += level.get("xp", 0)
    return total_xp

def get_assigned_course(user_id):
    data = db.child("assignments").child(user_id).get().val()
    return data.get("course") if data else None

def has_completed_level(user_id, course, level_index):
    path = f"progress/{user_id}/{course}/level_{level_index}"
    return db.child(path).get().val() is not None

def learner_dashboard(user):
    st.title("🎓 Learner Dashboard")
    user_id = user.get("user_id") or user.get("localId")
    username = user.get("username", "Learner")

    assigned_course = get_assigned_course(user_id)

    if not assigned_course:
        st.warning("No course assigned yet. Please wait for your instructor to assign one.")
        return

    st.subheader(f"📚 Assigned Course: {assigned_course}")
    total_xp = get_user_xp(user_id)
    st.success(f"🌟 Total XP: {total_xp}")

    course = COURSES.get(assigned_course, {})
    if not course:
        st.error("Course data not found.")
        return

    st.markdown("---")
    st.subheader("📈 Progress & Quizzes")

    for idx, level in enumerate(course["levels"]):
        level_name = level["name"]
        completed = has_completed_level(user_id, assigned_course, idx)

        with st.expander(f"Level {idx + 1}: {level_name} {'✅' if completed else ''}"):
            if completed:
                st.info("Level already completed.")
            else:
                questions = QUIZ_QUESTIONS.get(assigned_course, {}).get(level_name, [])
                if not questions:
                    st.warning("No questions found for this level.")
                    continue

                answers = []
                for q in questions:
                    ans = st.text_input(f"Q: {q['question']}", key=f"{level_name}_{q['question']}")
                    answers.append(ans)

                if st.button(f"Submit Quiz - {level_name}", key=f"submit_{level_name}"):
                    if all(ans.strip() != "" for ans in answers):
                        result = take_quiz(user_id, assigned_course, level_name, answers)
                        st.success(f"✅ Submitted! Score: {result['score']}%, XP Earned: {result['xp_result']['xp']}")
                        st.experimental_rerun()
                    else:
                        st.warning("Please answer all questions.")
