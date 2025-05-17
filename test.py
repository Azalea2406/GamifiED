from Authentication.auth import signup_user, login_user, send_reset_email
from Learning.progress_tracker import submit_level, get_user_xp

# --- TEST 1: SIGNUP ---
print("\n---- Testing Sign Up ----")
signup_result = signup_user(
    email="testuser1@example.com",
    password="password123",
    role="student",
    username="testuser1"
)
print("Signup Result:", signup_result)

# --- TEST 2: LOGIN ---
print("\n---- Testing Login ----")
login_result = login_user("testuser1@example.com", "password123")
print("Login Result:", login_result)

if login_result["success"]:
    user = login_result["user"]
    user_id = login_result["user_id"]

    # --- TEST 3: SUBMIT LEVEL COMPLETION ---
    print("\n---- Testing Level Submission ----")
    level_submit = submit_level(user_id, level=1, earned_xp=50)
    print("Submit Level:", level_submit)

    # --- TEST 4: GET USER XP ---
    print("\n---- Testing XP Retrieval ----")
    xp_result = get_user_xp(user_id)
    print("XP Result:", xp_result)

# --- TEST 5: PASSWORD RESET (optional) ---
# print("\n---- Testing Password Reset ----")
# reset_result = send_reset_email("testuser1@example.com")
# print("Password Reset:", reset_result)
