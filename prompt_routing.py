from flask import Blueprint, request, jsonify, session, render_template, url_for
from supabase_character_CRUD import get_user_characters, read_character
from assignment import ask_gpt

prompt_bp = Blueprint('prompt', __name__, template_folder='templates')

@prompt_bp.route('/select_characters', methods=['GET', 'POST'])
def select_characters():
    characters = get_user_characters(session.get('firebase_uid'))
    json_path = url_for('static', filename='JSON/Animation---1709061657569.json')


    if request.method == 'POST':
        selected_character_ids = request.form.getlist('character_ids')
        selected_character_ids = [id for id in selected_character_ids if id]  # Ensure IDs are valid

        prompt = "You are a master level dungeon master for Dungeons and Dragons 5th edition. Help me make decisions for my party\n"
        prompt += "I want you to select three items in total for the following characters:\n"
        loot_types = request.form.getlist('loot_type')
        

        print(loot_types)
        if 'custom' in loot_types:
            prompt += "Use the 5th edition Dungeon Master's guide's rules for creating magical items to create custom items for these characters. Use items you make for this and not SRD items.\n"
        elif 'standard' in loot_types:
            prompt += "Select these items from the official dungeons and dragons 5th edition SRD\n"
        prompt += "The loot must be magical\n"
        for char_id in selected_character_ids:
            character = read_character(int(char_id))
            if character:
                # Constructing character info string with all attributes
                character_info = (f"Character Name: {character['name']}, Class: {character['class_name']}, "
                                  f"Subclass: {character.get('subclass_name', 'N/A')}, Race: {character['race']}, "
                                  f"Sub Race: {character.get('sub_race', 'N/A')}, Level: {character['level']}, "
                                  f"Strength: {character['strength_score']}, Dexterity: {character['dexterity_score']}, "
                                  f"Constitution: {character['constitution_score']}, Intelligence: {character['intelligence_score']}, "
                                  f"Wisdom: {character['wisdom_score']}, Charisma: {character['charisma_score']}, "
                                  f"Armor Class: {character['armor_class']}, Hit Points: {character['hit_points']}, "
                                  f"Background: {character['background_type']}.")
                prompt += character_info + "\n"
                
        prompt += "Again, always pick exactly three items for the party regardless of the number of characters. Assign items for the characters most in need of them.\n"
        prompt += "Ensure that these items a balanced for the characters so that they are not too strong or too weak. Items must be level appropriate as per the dungeon master's guide.\n"
        prompt += "Ensure the items are specifically tailored to each character's class and level, considering their racial background and subclass where applicable. Items should enhance the characters' attribute strengths and mitigate their weaknesses.\n"
        prompt += "Also please ensure that, while the loot is good, it is not always the best possible option to help improve improvisation and creativity. Turn down the temperature if necessary.\n"
        prompt += "Please spend most of your response listing the items and their characteristic and less about why you chose them.\n"
        prompt += "Please just list the items, and a number in the list, do not include a preamble or suffix.\n"
        prompt += "Please ensure that you always include an HTML line break in between each listed item.\n"
        response_text = ask_gpt(prompt, model="gpt-4")

        return jsonify({'gpt_response': response_text})

    return render_template('test_prompt_page.html', characters=characters, gpt_response="", json_path=json_path)