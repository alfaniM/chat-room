import re
import json

# Read the chat data from a text file
def read_chat_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()

# Parse the chat text
def parse_chat(chat_lines):
    messages = []
    for line in chat_lines:
        match = re.match(r"(\d{2}/\d{2}/\d{2} \d{2}\.\d{2}) - (.*?): (.*)", line)
        if match:
            timestamp, sender, message = match.groups()
            messages.append({
                "timestamp": timestamp.replace('.', ':'),  # Fix time format
                "sender": sender,
                "message": message
            })
    return messages

# Convert to JSON and save to a file
def save_to_json(chat_data, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(chat_data, file, indent=4, ensure_ascii=False)

def main():
    # Set the file paths
    input_file = "chat.txt"   # Replace with the path to your chat file
    output_file = "chat.json" # This is where the JSON will be saved

    # Step 1: Read chat data from the text file
    chat_lines = read_chat_file(input_file)

    # Step 2: Parse the chat data
    chat_data = parse_chat(chat_lines)

    # Step 3: Save the parsed data as a JSON file
    save_to_json(chat_data, output_file)

    print(f"Chat data has been successfully converted to {output_file}!")

if __name__ == "__main__":
    main()
