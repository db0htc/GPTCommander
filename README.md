### GPTCommander <p>

Simple API interface for ChatGPT, with a few basic features  

Make sure to replace "API_KEY_HERE" in the script with your actual API key.
</p>

#### Usage:

py T8.py

#### In-program commands

&ensp;&ensp;IMPORT [Filename]&ensp;&ensp;&ensp;&ensp; Imports a file into the chat. it will simply strip out or escape any odd characters and send the text into chat. Works best for source code files or text files. I've gotten it to read IC datasheets after stripping the odd characters out of it

&ensp;&ensp;QUIT&ensp;&ensp;&ensp;&ensp; Saves the history to hist.txt, saves a human readable chat log to Output.log, and automatically saves THE LAST python code in ChatGPT's last response to Last.py (all of which are saved to the same directory as T8.py)

#### Recommendations

I like to have a copy of T8.py in a dedicated folder with any project i'm working on, so i have a dedicated ChatGPT instance with a separate chat history for each project
