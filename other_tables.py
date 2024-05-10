# from supabase import create_client, Client
# from CONSTANTS import SUPABASE_URL, SUPABASE_KEY
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# from supabase import create_client

# supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# #read monsters
# def read_monster(ID_num):
#     response = supabase.table("SRD_Monsters").select("*").eq("id", ID_num).execute()

#     if response.data:  # Adjusted assuming 'data' is a property or method
#         monster_data = response.data

#         if monster_data:  # Further check if data is not empty
#             monster = monster_data[0]

#             # Extract and assign each piece of data to variables
#             id = monster.get('id')
#             name = monster.get('name')
#             alignment = monster.get('alignment')
#             armor_class = monster.get('armor_class')
#             armor_class_misc = monster.get('armor_class_misc')
#             strength = monster.get('strength')
#             strength_mod = monster.get('strength_mod')
#             dexterity = monster.get('dexterity')
#             dexterity_mod = monster.get('dexterity_mod')
#             constitution = monster.get('constitution')
#             constitution_mod = monster.get('constitution_mod')
#             intelligence = monster.get('intelligence')
#             intelligence_mod = monster.get('intelligence_mod')
#             wisdom = monster.get('wisdom')
#             wisdom_mod = monster.get('wisdom_mod')
#             charisma = monster.get('charisma')
#             charisma_mod = monster.get('charisma_mod')
#             CR = monster.get('CR')
#             condition_immunities = monster.get('condition_immunities')
#             damage_immunities = monster.get('damage_immunities')
#             damage_resistances = monster.get('damage_resistances')
#             hit_points = monster.get('hit_points')
#             languages = monster.get('languages')
#             type = monster.get('type')
#             saving_throws = monster.get('saving_throws')
#             senses = monster.get('senses')
#             skills = monster.get('skills')
#             speed = monster.get('speed')
#             xp_award = monster.get('xp_award')

#             # Print statement for debugging purposes
#             print(f"ID: {id}, Name: {name}, Alignment: {alignment}, Armor Class: {armor_class} {armor_class_misc}, Strength: {strength} {strength_mod}, Dexterity: {dexterity} {dexterity_mod}, Constitution: {constitution} {constitution_mod}, Intelligence: {intelligence} {intelligence_mod}, Wisdom: {wisdom} {wisdom_mod}, Charisma: {charisma} {charisma_mod}, CR: {CR}, Condition Immunities: {condition_immunities}, Damage Immunities: {damage_immunities}, Damage Resistances: {damage_resistances}, Hit Points: {hit_points}, Languages: {languages}, Type: {type}, Saving Throws: {saving_throws}, Senses: {senses}, Skills: {skills}, Speed: {speed}, XP Award: {xp_award}")
#         else:
#             print("Monster data is empty")
#     else:
#         print("Response did not contain any data")

# # Adjust the function call based on your specific needs
# read_monster(15)


# #read spells
# def read_spell(ID_num):
#     response = supabase.table("spells").select("*").eq("id", ID_num).execute()

#     if response.data:  # Adjusted assuming 'data' is a property or method
#         spell_data = response.data

#         if spell_data:  # Further check if data is not empty
#             spell = spell_data[0]

#             # Extract and assign each piece of data to variables
#             id = spell.get('id')
#             name = spell.get('name')
#             casting_time = spell.get('casting_time')
#             component_material = spell.get('component_material')
#             component_sematic = spell.get('component_sematic')
#             component_verbal = spell.get('component_verbal')
#             component_misc = spell.get('component_misc')
#             description = spell.get('description')
#             duration = spell.get('duration')
#             level = spell.get('level')
#             range = spell.get('range')
#             range_area = spell.get('range_area')
#             school = spell.get('school')
#             school_ritual = spell.get('school_ritual')
#             casting_time_misc = spell.get('casting_time_misc')

#             # Print statement for debugging purposes
#             print(f"ID: {id}, Name: {name}, Casting Time: {casting_time}, Component Material: {component_material}, Component Sematic: {component_sematic}, Component Verbal: {component_verbal}, Component Misc: {component_misc}, Description: {description}, Duration: {duration}, Level: {level}, Range: {range}, Range Area: {range_area}, School: {school}, School Ritual: {school_ritual}, Casting Time Misc: {casting_time_misc}")
#         else:
#             print("Spell data is empty")
#     else:
#         print("Response did not contain any data")

# # Adjust the function call based on your specific needs
# read_spell(15)