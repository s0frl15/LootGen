import pyrebase
import logging
from firebase_admin import auth
from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY
from flask import current_app, session
from auth_key import initialize_firebase_admin

# Initialize the Supabase client with provided URL and key, enabling interaction with Supabase services.
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Initialize the Firebase Admin SDK to allow server-side Firebase user management.
initialize_firebase_admin()

# Set up basic logging configuration for easier debugging and monitoring.
logging.basicConfig(level=logging.INFO)

def get_firebase_auth():
    # Initialize the Firebase app using the config from the current Flask application context and return the auth instance.
    firebase = pyrebase.initialize_app(current_app.config['FIREBASE_CONFIG'])
    return firebase.auth()

def create_user(email, password):
    # Create a new user in Firebase Authentication and log the success.
    user = auth.create_user(email=email, password=password)
    print(f'Successfully created new user: {user.uid}')

    # Insert the new user's Firebase UID into the Supabase 'user' table for linking data.
    response = supabase.table("user").insert({"firebase_uid": user.uid}).execute()

    # Check for errors in the Supabase response and log accordingly.
    if 'error' in response:
        error = response['error']
        logging.error(f"Error inserting user into Supabase: {error}")
    else:
        logging.info("User inserted into Supabase successfully.")

    # Return the Firebase user object for further use if needed.
    return user

from flask import session

def sign_in_user(email, password):
    # Clear the existing session to remove any previous user's data
    session.clear()

    # Get the Firebase auth instance for the current Flask application context.
    auth = get_firebase_auth()
    try:
        # Sign in the user with Firebase Authentication and store their UID in the session.
        user = auth.sign_in_with_email_and_password(email, password)
        session['firebase_uid'] = user['localId']  # 'localId' is typically the key for the UID in Firebase's response.
        logging.info(f"User signed in successfully with UID: {session['firebase_uid']}.")
        return user
    except Exception as e:
        # Log any sign-in errors and return None to indicate failure.
        logging.error(f"Failed to sign in: {e}")
        return None


def reauthenticate_user(email, password):
    # Reauthenticate a user with Firebase Authentication.
    auth = get_firebase_auth()
    try:
        # Attempt to sign in the user again as a form of reauthentication.
        user = auth.sign_in_with_email_and_password(email, password)
        # If successful, return True indicating the user is reauthenticated.
        return True
    except Exception as e:
        # Log any errors encountered during reauthentication.
        logging.error(f"Error re-authenticating user: {str(e)}")
        return False
