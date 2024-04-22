#1
import pandas as pd
from bs4 import BeautifulSoup
import uuid
import re
# Reads HTML file(the html has to be in the same directory as the script)
with open('sample.html.html', 'r', encoding='utf-8') as f:
    html_string = f.read()
    #2
# Parses the HTML using BeautifulSoup
soup = BeautifulSoup(html_string, 'html.parser')
#3
# Extracts user id, timestamp, message prompt, image url, and '@' mentions for each chat message
user_ids = []
timestamps = []
message_prompts = []
image_urls = []
mentions = []

users = {}
user_count = 0

for message in soup.find_all('div', class_='chatlog__message'):
    user_elem = message.find('span', class_='chatlog__author')
    if user_elem and 'data-user-id' in user_elem.attrs:
        user_id = user_elem['data-user-id']
    else:
        user_id = None
    user_ids.append(user_id)

    timestamp_elem = message.find('span', class_='chatlog__timestamp')
    if timestamp_elem:
        timestamp_a_elem = timestamp_elem.find('a')
        if timestamp_a_elem:
            timestamp = timestamp_a_elem.text.strip()
        else:
            timestamp = timestamp_elem.text.strip()
    else:
        timestamp = None
    timestamps.append(timestamp)

    message_elem = message.find('span', class_='chatlog__markdown-preserve')
    if message_elem:
        message_prompt = message_elem.text.strip()
        # Extracts '@' mentions from message prompt
        mention_pattern = r'@([^\s]+)'
        mention_matches = re.findall(mention_pattern, message_prompt)
        pseudonyms = []
        for mention in mention_matches:
            if mention not in users:
                user_count += 1
                users[mention] = f'user {user_count}'
            pseudonyms.append(users[mention])
        mentions.append(pseudonyms)
        # Removes '@' mentions from message prompt
        message_prompt = re.sub(mention_pattern, '', message_prompt)
    else:
        message_prompt = None
        mentions.append(None)
    message_prompts.append(message_prompt)

    image_elem = message.find('img', class_='chatlog__avatar')
    if image_elem and 'src' in image_elem.attrs:
        image_url = image_elem['src']
    else:
        image_url = None
    image_urls.append(image_url)

# Creates a DataFrame from the extracted data points
data = {
    'user_id': user_ids,
    'timestamp': timestamps,
    'message_prompt': message_prompts,
    'image_url': image_urls,
    'mentions': mentions
}
df = pd.DataFrame(data)

# Prints the DataFrame
print(df)

# Saves the DataFrame to a CSV file
df.to_csv('chatlog.csv', index=False)
