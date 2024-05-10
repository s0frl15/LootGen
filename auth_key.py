import firebase_admin
from firebase_admin import credentials

def initialize_firebase_admin():
    cred_path = 'firebase_key.json'
    cred = credentials.Certificate(cred_path)
    
    # Initialize Firebase if it hasn't been initialized yet.
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)