# Firebase Auth code goes here
import pyrebase
from datetime import datetime

firebase_config = {
    "apiKey": "AIzaSyBAxO8ACbviAbFZEopMiW-MD5WZX17TE4c",
    "authDomain": "gamified-2064.firebaseapp.com",
    "databaseURL": "https://gamified-2064-default-rtdb.firebaseio.com/",
    "projectId": "gamified-2064",
    "storageBucket": "gamified-2064.appspot.com",
    "messagingSenderId": "408735255781",
    "appId": "1:408735255781:web:fc9e41339a6feea8e1180c",
    "measurementId": "G-1JLQ89LZPC"
}

#Initialize Firebase

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth() #handles authentication(login and signup
db = firebase.database() #db accesses the Firebase Realtime Database (not Firestore)

#User Sign-up
def signup_user(email, password, role, username):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        user_id = user['localId'] # creates new user account in firebase. Firebase then returns a localID (unique userID)
       
        # Store user info in Firestore/Realtime DB
        db.child("users").child(user_id).set({
            "email": email,
            "role": role,
            "username": username,
            "created_at": str(datetime.now())
        }) # store email, role, username and signup

        return {"success": True, "user_id": user_id}
    except Exception as e:
        return {"success": False, "error": str(e)}

#User Login
def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        user_id = user['localId'] # logs in the user and gets their id

        user_info = db.child("users").child(user_id).get().val()
        return {"success": True, "user": user_info} #Fetches the user's saved data (role, username, etc.) from Firebase
    
    except Exception as e: #Handles incorrect password, email not found, etc.
        return {"success": False, "error": str(e)}

# Forgot password
def send_reset_email(email):
    try:
        auth.send_password_reset_email(email)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
