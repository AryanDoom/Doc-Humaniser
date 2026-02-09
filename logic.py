import random
import json


def generate_keystroke_log(text):
    log = []
    for char in text:
        # 1. Add the actual character
        log.append({"action": "type", "char": char, "delay": random.uniform(50, 150)})
        
        # 2. Add "Human Noise": 2% chance of a typo
        if random.random() < 0.02:
            wrong_char = random.choice('qwertyuiop')
            log.append({"action": "type", "char": wrong_char, "delay": random.uniform(50, 100)})
            log.append({"action": "backspace", "delay": random.uniform(200, 400)})
            
        # 3. Add "Thinking Pauses" every few words
        if char == ' ' and random.random() < 0.1:
            log.append({"action": "wait", "delay": random.uniform(1000, 3000)})

    with open('keystrokes.json', 'w') as f:
        json.dump(log, f)
    print("Pattern generated! Copy the contents of keystrokes.json into the extension.")

# Paste your AI text here
essay = "The industrial revolution changed the world..."
generate_keystroke_log(essay)