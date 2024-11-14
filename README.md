# Article Creator: GPT-Powered Article Generator

This application leverages OpenAI's API to generate HTML-formatted articles based on user input. The user provides a concept or idea for an article in a text file (`input.txt`), and the app generates a full article that follows a basic HTML structure, with image placeholders for the content team.

## Features

- Reads article ideas from an `input.txt` file.
- Uses **GPT-4o-mini** to generate a structured article in basic HTML markup.
- Writes the output article to a file called `artykul.html`.
- Includes image placeholders (`<img>`) with alt text to guide the image team.
- Follows a predefined system prompt to ensure content adheres to a specific format.

## Requirements

- Python 3.12.6 or higher.
- OpenAI API key.

## Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/filipmachalowski/ArticleCreator
cd article-creator
```

### 2. Install Dependencies

Ensure Python is installed, then install the required libraries using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Set Up OpenAI API Key

Create a `.env` file in the project root directory and add your OpenAI API key:

```bash
OPENAI_API_KEY="your_openai_api_key_here"
```

You can obtain an API key by signing up at [OpenAI](https://platform.openai.com/signup).

### 4. Prepare the Input

Modify `input.txt` in the project directory with your own article idea.

### 5. Run the Application

Once everything is set up, run the Python script:

```bash
python articlecreator.py
```

### 6. Output

The generated article will be saved in `artykul.html`. The file will be overwritten each time the script runs, so only the latest generated article will be saved.

## Customization

You can easily customize the generated article by modifying the script or adjusting the prompt. For example:

- Modify the `prompt` variable in the script to change how **GPT-4o-mini** responds to user input.
- Customize the HTML structure or image placeholder instructions to fit your project's needs.

## Troubleshooting

- **API Key Missing**: Ensure the OpenAI API key is properly set in the `.env` file.
- **File Not Found**: Make sure `input.txt` exists in the same directory as the script.

If you encounter any issues or have questions, feel free to open an issue on this repository!

## License

The software is provided under a license for personal, academic, or non-commercial use. Commercial use is permitted only for testing purposes, which includes using the software to evaluate, test, or assess its performance, functionality, or suitability in a non-production environment. Use of the software for profit in any production environment, including but not limited to integration into commercial products or services, requires a separate commercial license.
A commercial license may be subject to a fee, including a percentage of revenue from products or services that incorporate this software. Please contact the repository owner for commercial licensing terms.
