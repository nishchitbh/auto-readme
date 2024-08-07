# Auto-README Generator

This script automatically generates a README.md file for a repository using the Gemini Pro model from Google AI. It analyzes the code within the repository and creates a comprehensive README file based on its understanding.

## Features

- **Code Analysis:** Reads and understands code from various file types (c, cpp, py, js, ts, java, rs).
- **Gemini Pro Integration:** Leverages the power of the Gemini Pro model for advanced code comprehension and README generation.
- **Recursive File Reading:** Recursively explores the repository directory to include all relevant code files.
- **Customizable Instructions:** Allows for customization through a `sys_instruction.txt` file to guide the model's behavior.
- **History Management:** Utilizes a `history.json` file to maintain context and improve the model's performance over time.

## Requirements

- **Python:** Ensure you have Python installed.
- **Google Cloud Project:** Set up a Google Cloud Project and enable the Generative AI API.
- **API Key:** Obtain a Google API key and store it securely in a `.env` file as `GEMINI_API_KEY`.
- **Required Packages:** Install the necessary packages:

  ```bash
  pip install google-generativeai python-dotenv colorama
  ```

## Usage

1. **Configuration:**
   - Create a `sys_instruction.txt` file to provide specific instructions to the Gemini Pro model regarding the desired content and format of the README.md file.
   - (Optional) Create a `history.json` file to store previous interactions with the model, allowing for better context and improved results over time.

2. **Run the script:**
   ```bash
   python auto_readme.py
   ```

## How it Works

1. **Initialization:**
   - Loads environment variables from the `.env` file.
   - Configures the Google Generative AI API with the provided API key.
   - Initializes a chat session with the Gemini Pro model, using the instructions from `sys_instruction.txt` and history from `history.json` (if available).

2. **Code Extraction:**
   - Recursively reads all code files within the repository directory, excluding specified ignored directories (e.g., `venv`, `.git`).
   - Filters files based on supported extensions (c, cpp, py, js, ts, java, rs).
   - Stores the content of each file in a dictionary.

3. **README Generation:**
   - Converts the code dictionary into a JSON string.
   - Sends the JSON string to the Gemini Pro model through the chat session.
   - Receives the generated README.md content from the model.

4. **File Writing:**
   - Writes the generated README.md content to a file named `README.md` in the repository's root directory.

## Customization

- **`sys_instruction.txt`:** This file allows you to customize the behavior of the Gemini Pro model by providing specific instructions. For example:

   ```
   You are a helpful AI assistant that generates README files for code repositories.
   Please include the following sections in the README:
   - Title
   - Description
   - Features
   - Requirements
   - Usage
   - How it Works
   - Customization (if applicable)
   - Examples (if applicable)
   - Notes (if applicable)
   ```

- **`history.json`:** This file can be used to store previous interactions with the model, allowing for better context and potentially improved results over time.

## Important Notes

- Ensure that the `GEMINI_API_KEY` is correctly set in the `.env` file.
- The quality of the generated README.md file depends on the clarity and structure of the code, as well as the instructions provided in `sys_instruction.txt`.
- Review the generated README.md file to ensure accuracy and completeness.
- Remember to configure billing for your Google Cloud Project to avoid unexpected charges.

This project is licensed under the MIT License.
