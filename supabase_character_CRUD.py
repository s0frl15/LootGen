from supabase import create_client, Client
import logging
from config import SUPABASE_URL, SUPABASE_KEY

# Create a Supabase client using the provided URL and API key from the config. This client allows you to interact with your Supabase database.
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def create_character(firebase_uid, strength_score, dexterity_score, constitution_score, intelligence_score, wisdom_score, charisma_score, armor_class, hit_points, level, name, background_type, class_name, subclass_name, race, sub_race):
    # Log the action of attempting to create a new character, identifying the operation by the user's Firebase UID.
    logging.info(f"Attempting to create character with Firebase UID: {firebase_uid}")
    
    # Query the Supabase database to find a user_id that matches the provided Firebase UID.
    user_response = supabase.table("user").select("user_id").eq("firebase_uid", firebase_uid).execute()
    
    # Check for errors in the user query response, such as not finding the user or database errors.
    if 'error' in user_response:
        logging.error(f"Failed to find user in Supabase: {user_response['error']}")
        return "Error: User not found in Supabase", 404

    # If the query didn't return any data, it means the user was not found in the database.
    if not user_response.data:
        logging.info("No data returned from Supabase")
        return "Error: User not found in Supabase", 404

    # Extract the user_id from the query's response. This ID will be used to link the character to the user.
    supabase_user_id = user_response.data[0]['user_id']
    logging.info(f"Found Supabase user ID: {supabase_user_id}, proceeding with character creation.")
    
    # Prepare the character data for insertion into the database. This includes all character attributes and the user_id for ownership.
    character_data = {
        "strength_score": strength_score,
        "dexterity_score": dexterity_score,
        "constitution_score": constitution_score,
        "intelligence_score": intelligence_score,
        "wisdom_score": wisdom_score,
        "charisma_score": charisma_score,
        "armor_class": armor_class,
        "hit_points": hit_points,
        "level": level,
        "name": name,
        "background_type": background_type,
        "class_name": class_name,
        "subclass_name": subclass_name,
        "race": race,
        "sub_race": sub_race,
        "user_owner": supabase_user_id
    }

    # Insert the character data into the "character" table in Supabase and check for errors.
    response = supabase.table("character").insert(character_data).execute()
    if 'error' in response:
        logging.error(f"Error creating character in Supabase: {response['error']}")
        return "Error: Failed to create character in Supabase", 500

    # If everything goes well, log and return a success message.
    logging.info("Character created successfully in Supabase.")
    return "Character created successfully", 200

def get_user_characters(firebase_uid):
    # Attempt to retrieve characters associated with a specific Firebase UID.
    logging.info(f"Attempting to fetch characters for Firebase UID: {firebase_uid}")
    
    # Find the user in the "user" table by their Firebase UID to get the Supabase user_id.
    user_response = supabase.table("user").select("user_id").eq("firebase_uid", firebase_uid).execute()
    
    # If the user doesn't exist or an error occurs, return None to indicate failure.
    if not user_response.data:
        logging.info("User not found in Supabase.")
        return None

    # Extract the Supabase user_id from the response.
    supabase_user_id = user_response.data[0]['user_id']
    logging.info(f"Supabase user ID associated with Firebase UID {firebase_uid}: {supabase_user_id}")
    
    # Retrieve all characters that belong to the user, using the Supabase user_id.
    characters_response = supabase.table("character").select("*").eq("user_owner", supabase_user_id).execute()
    
    # If characters are found, return them, otherwise log and return None.
    if characters_response.data:
        logging.info(f"Characters retrieved successfully for Supabase user ID {supabase_user_id}.")
        return characters_response.data
    else:
        logging.info(f"No characters found for Supabase user ID {supabase_user_id}.")
        return None

def read_character(char_id: int):
    # Attempt to read and return details of a specific character by their ID.
    logging.info(f"Attempting to read character with ID: {char_id}")
    
    # Query the "character" table for a character with the matching ID.
    query = supabase.table("character").select("*").eq("character_id", char_id).execute()
    
    # If character data is found, return it, otherwise log and return None.
    if query.data:
        logging.info(f"Character data retrieved for ID {char_id}: {query.data}")
        return query.data[0]  # Assuming only one character should match the ID.
    else:
        logging.info(f"No data returned from query for character ID {char_id}.")
        return None

def update_character(char_id, strength_score, dexterity_score, constitution_score, intelligence_score, wisdom_score, charisma_score, armor_class, hit_points, level, name, background_type, class_name, subclass_name, race, sub_race):
    # Log the attempt to update a character's details in the database.
    logging.info(f"Updating character with ID: {char_id}")
    
    # Execute an update operation for a character with the given ID, altering only the specified fields.
    result = supabase.table("character").update({
        "strength_score": strength_score,
        "dexterity_score": dexterity_score,
        "constitution_score": constitution_score,
        "intelligence_score": intelligence_score,
        "wisdom_score": wisdom_score,
        "charisma_score": charisma_score,
        "armor_class": armor_class,
        "hit_points": hit_points,
        "level": level,
        "name": name,
        "background_type": background_type,
        "class_name": class_name,
        "subclass_name": subclass_name,
        "race": race,
        "sub_race": sub_race
    }).eq("character_id", char_id).execute()

    # Return the update operation result.
    return result

def delete_character(char_id):
    # Log the attempt to delete a character by their ID.
    logging.info(f"Deleting character with ID: {char_id}")
    
    # Perform the deletion operation for the character with the specified ID.
    result = supabase.table("character").delete().eq("character_id", char_id).execute()

    # Check the result of the deletion operation and return True for success or False for failure.
    # if result.error:
    #     logging.error(f"Error deleting character: {result['error']}")
    #     return False
    return True
