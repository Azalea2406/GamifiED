from Authentication.auth import signup_user, login_user
from Learning.quiz_submission import submit_quiz
from ui.dashboard_page import get_user_xp

print("------ TEST: Sign Up ------")
signup = signup_user("quizuser@example.com", "securePass123", "student", "quizUser")
print(signup)

if signup["success"]:
    print("------ TEST: Login ------")
    login = login_user("quizuser@example.com", "securePass123")
    print(login)

    if login["success"]:
        user_id = login["user_id"]

        print("------ TEST: Submit Quiz ------")
        result = submit_quiz(user_id, "Python Basics", 0, correct_answers=4)
        print(result)

        print("------ TEST: Get XP ------")
        xp = get_user_xp(user_id)
        print(f"Total XP: {xp}")

