import os
import json
from colorama import Fore
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# This code generates a README.md file for a repository by using the Gemini Pro model and extracting the code from all files in the repository. 
# The process involves initializing the chat session with Gemini Pro, reading all code files recursively, generating a README.md using the chat session, and writing it to the file. 
def chatModel():
    '''Initializes a chat session with Gemini Pro model.
    Args:
        None
    Returns:
        obj: chat session object. '''
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192*2,
        "response_mime_type": "text/plain",
    }
    with open("sys_instruction.txt", "r") as f:
        sys_instruction = f.read()
    with open("history.json", "r") as f:
        history = json.load(f)
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-exp-0801",
        generation_config=generation_config,
        system_instruction=sys_instruction
    )
    chat_session = model.start_chat(
        history=history
    )
    return chat_session

def readmeGenerator(chat, file):
    '''Generates README.md content using Gemini Pro model and provided code.
    Args:
        obj: chat session object.
        str: code string.
    Returns:
        str: README.md content. '''
    response = chat.send_message(file)
    readme = response.text
    return readme

def extension_check(filename:str):
    '''Checks if the filename has a valid extension.
    Args:
        str: filename.
    Returns:
        bool: True if the filename has a valid extension, False otherwise. '''
    valid = ["c", "cpp", "py", "js", "ts", "java", "rs"]
    return filename.split(".")[-1] in valid


def read_files_recursively(root_dir):
    '''Reads all code files recursively from the given directory.
    Args:
        str: root directory path.
    Returns:
        dict: dictionary of file paths and their content. '''
    ignore = ["venv", ".git"]
    files_content = {}
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ignore]
        files = list(filter(extension_check, files))
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                files_content[file_path] = f.read()

    return files_content


def main():
    '''Main function to generate README.md file.
    Args:
        None
    Returns:
        None '''
    print(f"{Fore.GREEN}Generating README.md...{Fore.WHITE}")
    root_dir = '.'
    files_content = read_files_recursively(root_dir)
    code_json = json.dumps(files_content, indent=4, ensure_ascii=False)
    with open("README.md", "w") as readme:
        readme.write(readmeGenerator(chatModel(), code_json))
main()
