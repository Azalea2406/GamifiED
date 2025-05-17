import pyrebase

# Firebase configuration - Replace with your own Firebase project credentials
firebase_config = {
    "apiKey": "AIzaSyBAxO8ACbviAbFZEopMiW-MD5WZX17TE4c",
    "authDomain": "gamified-2064.firebaseapp.com",
    "databaseURL": "https://gamified-2064-default-rtdb.firebaseio.com", 
    "projectId": "gamified-2064",
    "storageBucket": "gamified-2064.firebasestorage.app",
    "messagingSenderId": "408735255781",
    "appId": "1:408735255781:web:fc9e41339a6feea8e1180c",
    "measurementId": "G-1JLQ89LZPC"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

def signup_user(email, password, role, username):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        user_id = user["localId"]
        # Save user data in Firebase Realtime Database
        db.child("users").child(user_id).set({
            "email": email,
            "role": role,
            "username": username
        })
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        user_id = user["localId"]
        user_data = db.child("users").child(user_id).get().val()
        return {"success": True, "user": user_data}
    except Exception as e:
        return {"success": False, "error": str(e)}
def send_reset_email(email):
    try:
        auth.send_password_reset_email(email)
        return {"status": "success", "message": f"Reset link sent to {email}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}