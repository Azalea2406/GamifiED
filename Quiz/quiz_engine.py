from Quiz.quiz_data import QUIZ_QUESTIONS
from Learning.progress_tracker import submit_level

def take_quiz(user_id, course_name, level_name, answers):
    from Learning.course_data import COURSES
    from Quiz.quiz_data import QUIZ_QUESTIONS
    from Learning.progress_tracker import submit_level

    questions = QUIZ_QUESTIONS.get(course_name, {}).get(level_name, [])
    correct = 0
    feedback = []

    for q, user_ans in zip(questions, answers):
        correct_answer = q["answer"].strip()
        user_clean = user_ans.strip()
        is_correct = correct_answer.lower() == user_clean.lower()
        if is_correct:
            correct += 1
        feedback.append({
            "question": q["question"],
            "your_answer": user_clean,
            "correct_answer": correct_answer,
            "is_correct": is_correct
        })

    score = (correct / len(questions)) * 100 if questions else 0
    level_index = get_level_index(course_name, level_name)

    result = submit_level(user_id, course_name, level_index, score)
    return {
        "total_questions": len(questions),
        "correct": correct,
        "score": score,
        "xp_result": result,
        "feedback": feedback
    }
