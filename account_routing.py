from flask import Blueprint, session, render_template, request, redirect, url_for
from firebase_auth import create_user, sign_in_user, reauthenticate_user
from firebase_admin import auth as admin_auth
from auth_key import initialize_firebase_admin
from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

# Initialize the Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Setting up a Flask Blueprint
auth_bp = Blueprint('auth', __name__, template_folder='templates')

# Route for the homepage.
@auth_bp.route('/')
def home():
    return render_template('index.html')

# Welcome page route. Checks if user is in session to display user-specific page, otherwise redirects to home.
@auth_bp.route('/welcome')
def welcome():
    user_email = session.get('user')
    if user_email:
        return render_template('user_page.html', user_email=user_email)
    return redirect('/')

# Login route. Supports both GET to display the login form and POST for form submission and authentication.
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = sign_in_user(email, password)
        if user:
            session['user'] = email  # On success, store user in session and redirect to welcome page.
            return redirect(url_for('auth.welcome'))
        else:
            return 'Failed to login'  # Login failure message.
    return render_template('login.html')  # Show the login form on GET request.

# Signup route.
@auth_bp.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = create_user(email, password)  # Attempt to create a new user.
            if user:
                session['user'] = email  # Store new user in session and redirect.
                return redirect(url_for('auth.welcome'))
        except Exception as e:
            # If user creation fails, return an error message.
            return 'This email already exists or another error occurred', 400
    return render_template('signup.html')  # Show the signup form on GET request.

# Logout route. Clears the user and firebase_uid from the session.
@auth_bp.route('/logout', methods=['POST'])
def logout():
    # Clear the entire session on logout
    session.clear()
    return redirect('/')

# Account deletion route. Requires user reauthentication for security.
@auth_bp.route('/delete-account', methods=['POST'])
def delete_account():
    initialize_firebase_admin()  # Necessary to interact with Firebase Admin SDK
    
    if 'user' in session:
        email = session['user']
        password = request.form.get('password')
        
        if reauthenticate_user(email, password):  # Reauthenticate before proceeding with deletion.
            try:
                user_record = admin_auth.get_user_by_email(email)
                admin_auth.delete_user(user_record.uid)  # Delete the user from Firebase Auth.
                
                # Attempt to delete user from Supabase as well.
                response = supabase.table("user").delete().eq("firebase_uid", user_record.uid).execute()

                if 'error' in response:
                    # Log any errors encountered during Supabase deletion.
                    error = response['error']
                    print(f"Error deleting user from Supabase: {error}")
                
                session.pop('user', None)  # Clear user session after deletion.
                return redirect(url_for('auth.welcome'))
            except Exception as error:
                # Handle any exceptions during the deletion process.
                return f"Account deletion failed: {str(error)}", 500
        else:
            # Response if reauthentication fails.
            return "Invalid password. Account deletion cancelled.", 401
    return redirect(url_for('auth.login'))  # Redirect to login if the session doesn't contain a user.
