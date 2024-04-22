README.md for Chatlog Parser
Overview
This Python script parses chatlog data from an HTML file using BeautifulSoup and extracts valuable information such as user IDs, timestamps, message prompts, image URLs, and mentions. The data is then organized into a pandas DataFrame and exported to a CSV file, making it easy to analyze chat interactions and trends.

Installation
To run this script, you need Python installed on your system along with some additional libraries. You can install the required libraries using pip:

pip install pandas beautifulsoup4

Usage
Prepare your HTML file: Ensure your chatlog HTML file is named sample.html and is located in the same directory as the script.
Run the script: Execute the script in your Python environment:

python chatlog_parser.py

Check the output: After running, the script will print the DataFrame to the console and save it to chatlog.csv in the current directory.
Data Output
The script extracts the following data points from each chat message in the HTML:

user_id: Unique identifier for the user.
timestamp: Timestamp of the chat message.
message_prompt: Text content of the message, excluding '@' mentions.
image_url: URL of any image associated with the message.
mentions: List of pseudonymized user IDs mentioned in the message.
Contributing
Feel free to fork this repository and submit pull requests with enhancements or fixes. For major changes, please open an issue first to discuss what you would like to change.

License
This project is open source and available under the MIT License.
