import logging
import openai
from config import GPTKEY

openai.api_key = GPTKEY

def ask_gpt(prompt, model="gpt-4"):
    logging.info(f"Sending prompt to OpenAI: {prompt[:1000]}...")
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        if response.choices:
            generated_text = response.choices[0].message['content'].strip()
            logging.info("Received response from OpenAI.")
            return generated_text
        else:
            logging.warning("No response received from OpenAI.")
            return "No response received."
    except Exception as e:
        logging.error(f"An error occurred while querying OpenAI: {e}")
        return ""
