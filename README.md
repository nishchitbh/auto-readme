# Auto-README Generator

This script automatically generates a `README.md` file for a repository by leveraging the power of the Gemini Pro model. It analyzes the code within the repository and creates a comprehensive README file that includes relevant information about the project.

## Features

- **Automated README Generation:**  Automatically generates a `README.md` file based on the code in the repository.
- **Gemini Pro Integration:** Utilizes the advanced capabilities of the Gemini Pro model for accurate and insightful README generation.
- **Recursive Code Analysis:** Recursively reads and analyzes all code files within the specified directory.
- **Customizable System Instructions:** Allows tailoring the README generation process through a `sys_instruction.txt` file.
- **Support for multiple languages:** Supports c, cpp, py, js, ts, java, and rs.

## Requirements

- **Python:** Ensure you have Python installed.
- **Google Cloud Project:** Set up a Google Cloud Project and enable the Generative AI API.
- **API Key:** Obtain a Google API key and store it securely in a `.env` file as `GEMINI_API_KEY`.
- **Required Packages:** Install the necessary packages:

  ```bash
  pip install google-generativeai python-dotenv colorama
  ```

## Usage

1. **Place the script in your repository's root directory.**
2. **Configure the `sys_instruction.txt` file with specific instructions for README generation.**
3. **Run the script:**

   ```bash
   python auto_readme.py
   ```

## Configuration

- **`sys_instruction.txt`:** This file contains instructions for the Gemini Pro model, allowing you to customize the README generation process. You can specify the desired sections, formatting, and level of detail.

- **`history.json`:** This file contains the history of the conversation with the Gemini Pro model. It is used to maintain context and improve the quality of the generated README.

## How it Works

1. **Initialization:** The script initializes a chat session with the Gemini Pro model.
2. **Code Analysis:** It recursively reads all code files within the repository's root directory.
3. **README Generation:** The script sends the code to the Gemini Pro model and receives the generated README content.
4. **File Writing:** The generated README content is written to a `README.md` file in the repository's root directory.

## Example `sys_instruction.txt`

```
You are a helpful AI assistant that generates README files for code repositories.
Analyze the provided code and create a comprehensive README.md file that includes the following sections:

- **Title:** A concise and descriptive title for the project.
- **Description:** A brief overview of the project's purpose and functionality.
- **Features:** A list of key features and capabilities.
- **Requirements:** A list of necessary dependencies and prerequisites.
- **Usage:** Clear instructions on how to use the project.
- **Configuration:** Details on any configuration options or settings.
- **Example:** Provide a simple example demonstrating the project's usage.
- **License:** Specify the license under which the project is distributed.
```

## Important Notes

- Ensure your `.env` file contains the `GEMINI_API_KEY`.
- The script currently supports several common programming languages. Support for other languages may be added in the future.
- The quality of the generated README depends on the clarity and structure of the code.
- Review the generated README to ensure accuracy and completeness.
- Remember to configure billing for your Google Cloud Project to avoid unexpected charges.

## License

This project is licensed under the MIT License.
