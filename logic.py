import random
import json
import os
from google import genai


def generate_keystroke_log(text):
    log = []
    for char in text:

        log.append({"action": "type", "char": char, "delay": random.uniform(50, 150)})

        if random.random() < 0.02:
            wrong_char = random.choice('qwertyuiop')
            log.append({"action": "type", "char": wrong_char, "delay": random.uniform(50, 100)})
            log.append({"action": "backspace", "delay": random.uniform(200, 400)})
            

        if char == ' ' and random.random() < 0.1:
            log.append({"action": "wait", "delay": random.uniform(1000, 3000)})

    with open('keystrokes.json', 'w') as f:
        json.dump(log, f)
    print("Pattern generated! Copy the contents of keystrokes.json into the extension.")


essay=""

client = genai.Client(api_key=os.getenv("DOOM_BOT_KEY"))

doom_instructions = """
You are a personal essay writer.
Do not be biased.
Do not use em dashes.
Make it sound humane.
Do not use emojis.
Do not use weird ahh words.
"""

def what_would_doom_write(user_input):

    prompt = f"""
{doom_instructions}

Write an essay on this:

{user_input}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash", # Updated to a valid model version
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    topic = input("Enter the topic for your essay: ")
    print(f"Generating human-like essay for: {topic}...")
    
    essay = what_would_doom_write(topic)
    
    if essay:
        print("\n--- Generated Essay preview ---")
        print(essay[:200] + "...")
        print("-------------------------------\n")
        
        generate_keystroke_log(essay)
    else:
        print("Failed to generate essay.")