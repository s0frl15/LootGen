from flask import Blueprint, request, redirect, url_for, render_template, jsonify, session
from supabase_character_CRUD import create_character, read_character, update_character, delete_character, get_user_characters

# Define a Blueprint
characters_bp = Blueprint('characters', __name__)

# Route to display the user's page. GET and POST methods are accepted but it primarily serves a static page.
@characters_bp.route('/user_page', methods=['GET', 'POST'])
def user_page():
    # Render and return the user_page.html template.
    return render_template('user_page.html')

# Route for handling character creation. Accepts both GET for form display and POST for form submission.
@characters_bp.route('/create_character', methods=['GET', 'POST'])
def handle_create_character():
    if request.method == 'POST':
        # Retrieve the Firebase UID from the user's session to link characters to users.
        firebase_uid = session.get('firebase_uid')
        if not firebase_uid:
            # Redirect to login if no UID is found, indicating no user is logged in.
            return redirect(url_for('auth.login'))

        # Collect form data for character creation.
        response, status_code = create_character(
            firebase_uid=firebase_uid,  # Using Firebase UID for user identification.
            strength_score=request.form.get('strength_score', type=int),
            dexterity_score=request.form.get('dexterity_score', type=int),
            constitution_score=request.form.get('constitution_score', type=int),
            intelligence_score=request.form.get('intelligence_score', type=int),
            wisdom_score=request.form.get('wisdom_score', type=int),
            charisma_score=request.form.get('charisma_score', type=int),
            armor_class=request.form.get('armor_class', type=int),
            hit_points=request.form.get('hit_points', type=int),
            level=request.form.get('level', type=int),
            name=request.form.get('name'),
            background_type=request.form.get('background_type'),
            class_name=request.form.get('class_name'),
            subclass_name=request.form.get('subclass_name'),
            race=request.form.get('race'),
            sub_race=request.form.get('sub_race')
        )

        # Check the status code of the character creation response.
        if status_code == 200:
            # Character creation was successful, redirect to the welcome page.
            return redirect(url_for('auth.welcome'))
        else:
            # Redirect back to the character creation form if there was an issue.
            return redirect(url_for('characters.handle_create_character'))
    else:
        # Display the character creation form for a GET request.
        return render_template('create_character.html')

# Route to display a list of characters belonging to the logged-in user.
@characters_bp.route('/user_characters')
def user_characters():
    firebase_uid = session.get('firebase_uid')
    if not firebase_uid:
        # Redirect to login if the user is not logged in (no Firebase UID in session).
        return redirect(url_for('auth.login'))

    # Fetch characters for the current user using their Firebase UID.
    characters = get_user_characters(firebase_uid)
    if characters:
        # Return the characters as a JSON response if found.
        return jsonify(characters)
    else:
        # Return an empty list if no characters are found.
        return jsonify([]), 404

# Route for showing detailed information about a specific character by their ID.
@characters_bp.route('/details/<int:char_id>')
def character_details(char_id):
    # Fetch detailed character information using the character ID.
    character_data = read_character(char_id)
    if character_data:
        # If the character is found, render and return the details page with the character data.
        return render_template('character_detail.html', character=character_data)
    else:
        # If no character is found, render an error page with an appropriate message.
        return render_template('error.html', message="Character not found"), 404

# Route to fetch and display a character's details by their ID, returning the data in JSON format.
@characters_bp.route('/character/<int:char_id>', methods=['GET'])
def read_character_route(char_id):
    # Attempt to fetch the character details using the character ID.
    character = read_character(char_id)
    if character:
        # If the character is found return the character data as JSON.
        return jsonify(character), 200
    else:
        # If the character is not found return an error message as JSON.
        return jsonify({"error": "Character not found"}), 404

# Route to handle updates to a character's details. Expects a JSON payload with the character's updated attributes.
@characters_bp.route('/update_character/<int:char_id>', methods=['POST'])
def handle_update_character(char_id):
    try:
        # Extract data from request JSON
        updated_data = request.json
        strength_score = updated_data.get('strength_score')
        dexterity_score = updated_data.get('dexterity_score')
        constitution_score = updated_data.get('constitution_score')
        intelligence_score = updated_data.get('intelligence_score')
        wisdom_score = updated_data.get('wisdom_score')
        charisma_score = updated_data.get('charisma_score')
        armor_class = updated_data.get('armor_class')
        hit_points = updated_data.get('hit_points')
        level = updated_data.get('level')
        name = updated_data.get('name')
        background_type = updated_data.get('background_type')
        class_name = updated_data.get('class_name')
        subclass_name = updated_data.get('subclass_name')
        race = updated_data.get('race')
        sub_race = updated_data.get('sub_race')

        # Call update_character function with individual attributes
        result = update_character(char_id, strength_score, dexterity_score, constitution_score, intelligence_score,
                                  wisdom_score, charisma_score, armor_class, hit_points, level, name, background_type,
                                  class_name, subclass_name, race, sub_race)

        return jsonify({"message": "Character updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to handle character deletion requests. Expects the character ID in the URL path.
@characters_bp.route('/delete_character/<int:char_id>', methods=['DELETE'])
def handle_delete_character(char_id):
    try:
        # Attempt to delete the character using the provided ID.
        if delete_character(char_id):
            # If deletion is successful, return a success message as JSON.
            return jsonify({"success": "Character deleted successfully"}), 200
        else:
            # If deletion fails, return an error message as JSON.
            return jsonify({"error": "Failed to delete character"}), 500
    except Exception as e:
        # If an unexpected error occurs, return an internal server error message as JSON.
        return jsonify({"error": "Internal server error"}), 500
