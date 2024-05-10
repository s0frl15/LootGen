# Import the necessary modules and configurations for the health checks.
from firebase_auth import get_firebase_auth  # For checking Firebase Authentication connectivity.
import openai  # For making requests to the OpenAI API.
from config import GPTKEY, SUPABASE_URL, SUPABASE_KEY  # Configuration values for APIs and database.
from supabase import create_client  # Supabase client for database operations.

# Initialize the Supabase client with the provided URL and Key from the configuration.
# This client is used for performing database operations within the health check functions.
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def database_health_check():
    try:
        # Perform a simple query to fetch a limited number of records from the 'user' table.
        response = supabase.table("user").select("firebase_uid").limit(1).execute()
        # If the query returns data, the database connectivity is considered successful.
        if response.data:
            return True, "Database connectivity check passed."
    except Exception as e:
        # If an exception occurs, it's captured and returned with a failure message.
        return False, f"Database connectivity check failed: {str(e)}"
    # If the query doesn't return data, consider it a failure.
    return False, "Database connectivity check failed: No data returned."

def external_api_health_check():
    # Set the API key for OpenAI.
    openai.api_key = GPTKEY
    try:
        # Make a test request to the OpenAI API.
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using 3.5 turbo for mindful token use.
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": "Hello, world!"}]
        )
        # If a response is received, the API connectivity check is considered successful.
        if response:
            return True, "OpenAI API connectivity check passed."
    except Exception as e:
        # Any exceptions are captured and considered a failure in connectivity.
        return False, f"OpenAI API connectivity check failed: {str(e)}"
    # If no response is received, it's considered a failure.
    return False, "OpenAI API connectivity check failed: No response."

def firebase_auth_check():
    try:
        # Attempt to get an instance of Firebase authentication.
        auth = get_firebase_auth()
        # If successful, return a positive result.
        if auth:
            return True, "Firebase authentication check passed."
    except Exception as e:
        # Capture and report any exceptions encountered during the process.
        return False, f"Firebase authentication check failed: {str(e)}"

    # If unable to get an auth instance, return a failure.
    return False, "Firebase authentication check failed."

# Main execution block for running the health checks when this script is executed directly.
if __name__ == "__main__":
    # Define a dictionary mapping health check names to their corresponding functions.
    checks = {
        "Database Connectivity": database_health_check,
        "OpenAI API Connectivity": external_api_health_check,
        "Firebase Authentication": firebase_auth_check,
    }

    # Flag to track the overall success of all health checks.
    all_passed = True
    # Iterate over each health check, execute it, and print the result.
    for name, func in checks.items():
        success, message = func()
        print(f"{name}: {message}")
        # If any check fails, set the flag to False.
        if not success:
            all_passed = False

    # Based on the flag, print the overall outcome of the health checks.
    if all_passed:
        print("All health checks passed successfully.")
    else:
        print("One or more health checks failed.")
