import json
import requests
import re

def read_file_to_json(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return {"role": "user", "content": content}

    return bytes(s, "utf-8").decode("unicode_escape")

API_KEY = "Bearer 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"

def main():
    history = []
    outputlog = []  # Initialize outputlog array

    # Try to load previous conversation history
    try:
        with open('hist.txt', 'r') as file:
            for line in file:
                history.append(json.loads(line.strip()))
    except FileNotFoundError:
        pass

    while True:
        user_input = input("You: ")
        outputlog.append("You: " + user_input)  # Add user input to outputlog
        if user_input == "QUIT":
            with open('hist.txt', 'w') as file:
                for item in history:
                    file.write(json.dumps(item) + '\n')

            # Save the last code block to a file
            code_regex = re.compile(r'```python(.*)```', re.DOTALL)
            last_code = None
            for log in reversed(outputlog):
                matches = code_regex.search(log)
                if matches:
                    last_code = matches.group(1)
                    break

            if last_code:
                with open('Last.py', 'w') as file:
                    file.write(last_code)

            # Save outputlog to Output.log
            with open('Output.log', 'w') as file:
                for item in outputlog:
                    file.write(item + '\n')

            break

        if user_input.startswith("IMPORT"):
            filename = user_input[7:]
            file_content = read_file_to_json(filename)
            history.append(file_content)
        else:
            history.append({"role": "user", "content": user_input})

        payload = {
            "model": "gpt-4-1106-preview",
            "messages": history,
            "temperature": 0
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": API_KEY,
                "Content-Type": "application/json"
            },
            json=payload
        )

        if response.status_code == 200:
            message = response.json()["choices"][0]["message"]["content"]
            print("ChatGPT: " + message)
            outputlog.append("ChatGPT: " + message)  # Add output to outputlog
            history.append({"role": "system", "content": message})
        else:
            print(f"API request failed with status code: {response.status_code}")
            outputlog.append(f"API request failed with status code: {response.status_code}")  # Add error message to outputlog
            return 1

    return 0

if __name__ == "__main__":
    main()