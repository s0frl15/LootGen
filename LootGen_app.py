# Import necessary modules and functions
from flask import Flask
import logging
from account_routing import auth_bp
from character_routing import characters_bp
from prompt_routing import prompt_bp
from config import FIREBASE_SECRET_KEY, FIREBASE_CONFIG
# Importing health check functions from a separate module
from health_checks import database_health_check, external_api_health_check, firebase_auth_check

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    
    # Set up logging for the application, specifying the format and level of logging details
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Configuration settings for Firebase and setting the application's secret key from the config
    app.config['FIREBASE_CONFIG'] = FIREBASE_CONFIG
    app.config['SECRET_KEY'] = FIREBASE_SECRET_KEY
    
    # Registering blueprints for organizing routes related to authentication, characters, and prompts into separate files
    app.register_blueprint(auth_bp)  # Authentication-related routes
    app.register_blueprint(characters_bp, url_prefix='/characters')  # Character management routes
    app.register_blueprint(prompt_bp, url_prefix='/prompt')  # Prompt handling routes

    return app

def run_health_checks():
    # Defining a dictionary of health checks to perform
    checks = {
        "Database Connectivity": database_health_check,
        "OpenAI API Connectivity": external_api_health_check,
        "Firebase Authentication": firebase_auth_check,
    }

    # Assume all checks will pass initially
    all_passed = True
    # Iterating over each health check, executing it, and logging the outcome
    for name, check_func in checks.items():
        success, message = check_func()
        logging.info(f"{name}: {message}")  # Log the message from each health check
        if not success:
            all_passed = False  # If any check fails, set all_passed to False

    return all_passed  # Return the overall result of health checks

if __name__ == '__main__':
    app = create_app()  # Create the Flask app with configurations and routes
    with app.app_context():  # Establish an application context for operations that require it, such as Firebase Auth checks
        # Perform health checks before starting the application server
        if run_health_checks():
            logging.info("All health checks passed. Starting application...")
            app.run(debug=True)  # Start the Flask application in debug mode if health checks pass
        else:
            logging.error("Application startup aborted due to failed health checks.")  # Log an error and abort startup if any checks fail
