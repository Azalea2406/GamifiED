from Authentication.auth import signup_user, login_user, send_reset_email
from Learning.progress_tracker import submit_level
from ui.dashboard_page import get_user_xp

# Credentials for test user
email = "testuser1@example.com"
password = "password123"
username = "testuser1"
role = "student"

# --- TEST 1: SIGNUP ---
print("\n---- Testing Sign Up ----")
signup_result = signup_user(email, password, role, username)
print("Signup Result:", signup_result)

# --- TEST 2: LOGIN ---
print("\n---- Testing Login ----")
login_result = login_user(email, password)
print("Login Result:", login_result)

if login_result["success"]:
    user_info = login_result["user"]
    user_id = user_info.get("user_id") or user_info.get("localId")

    if user_id:
        # --- TEST 3: SUBMIT LEVEL ---
        print("\n---- Testing Level Submission ----")
        submit_result = submit_level(user_id, "Python Basics", 0, 80)  # Submitting level 0 with score 80
        print("Level Submit Result:", submit_result)

        # --- TEST 4: GET XP ---
        print("\n---- Testing XP Retrieval ----")
        xp_result = get_user_xp(user_id)
        print("Total XP:", xp_result)

        # --- TEST 5: PASSWORD RESET (optional) ---
        print("\n---- Testing Password Reset ----")
        reset_result = send_reset_email(email)
        print("Password Reset:", reset_result)

    else:
        print("Login succeeded but user ID not found in response.")
else:
    print("Login failed:", login_result.get("error"))
