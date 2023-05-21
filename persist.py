import json
from datetime import datetime

filename = 'data.json'

def save_data(tweet_id, url, prompt, completion):
    data = {
        "created_at": datetime.now().strftime("%I:%M %p · %B %d, %Y"),
        "tweet_id": tweet_id,
        "url": url,
        "prompt": prompt,
        "completion": completion
    }

    try:
        with open(filename, 'r') as file:
            json_data = json.load(file) 
    except FileNotFoundError:
        json_data = []

    json_data.append(data) 

    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=4)  # 


def load_data():
    try:
        with open(filename, 'r') as file:
            json_data = json.load(file)
        return list(reversed(json_data)) 
    except FileNotFoundError:
        return []

