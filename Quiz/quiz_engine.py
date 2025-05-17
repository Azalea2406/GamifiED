from Quiz.quiz_data import QUIZ_QUESTIONS
from Learning.progress_tracker import submit_level

def take_quiz(user_id, course_name, level_name, answers):
    questions = QUIZ_QUESTIONS.get(course_name, {}).get(level_name, [])
    correct = 0

    for q, user_ans in zip(questions, answers):
        if q["answer"].strip().lower() == user_ans.strip().lower():
            correct += 1

    score = (correct / len(questions)) * 100 if questions else 0
    level_index = get_level_index(course_name, level_name)

    result = submit_level(user_id, course_name, level_index, score)
    return {
        "total_questions": len(questions),
        "correct": correct,
        "score": score,
        "xp_result": result
    }

def get_level_index(course, level_name):
    from Learning.course_data import COURSES
    levels = COURSES[course]["levels"]
    for idx, level in enumerate(levels):
        if level["name"] == level_name:
            return idx
    return -1
