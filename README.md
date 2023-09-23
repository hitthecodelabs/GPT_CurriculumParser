# GPT_CurriculumParser 

🚀 [**Live Demo of the Website**](https://gpt-curriculum-info-extractor.uc.r.appspot.com/)

Welcome to the GPT_CurriculumParser project! This Flask-based website provides information about our services in data science, machine learning, and AI. Below are step-by-step instructions to set up and run this project.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Cloning the Project](#cloning-the-project)
- [Setting Up OpenAI Key](#setting-up-openai-key)
- [Installing Dependencies](#installing-dependencies)
- [Running the Flask Application](#running-the-flask-application)

## Prerequisites
Before you begin, ensure you have the following installed on your system:
1. Python (Version 3.8 or above)
2. Git

## Cloning the Project
1. Open a terminal or command prompt.
2. Navigate to the directory where you want to clone the project.
3. Run the following command:

```bash
git clone https://github.com/hitthecodelabs/GPT_CurriculumParser.git
```

## Setting Up OpenAI Key
1. Locate the app.py file in the project's root directory.
2. Open app.py in your preferred text editor.
3. Find the variable named OPENAI_SECRET_KEY and replace 'YOUR_OPENAI_KEY_HERE' with your actual OpenAI API key:

```bash
import openai

openai.api_key = 'YOUR_OPENAI_KEY_HERE'
```

4. In the same app.py file, fill the prompt variable. Based on the context you provided, this will likely be a string that instructs OpenAI on what kind of response you are looking for. For example:
```bash
prompt = (f"Collect the following resume to extract structured information... ")
```

## Installing Dependencies
1. Navigate to the project's root directory in the terminal.
2. Create a virtual environment (recommended for isolated Python environments):

```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:

```bash
.\venv\Scripts\activate
```
- On  macOS and Linux:
```bash
source venv/bin/activate
```

4. Install the required libraries:
```bash
pip install -r requirements.txt
```

## Running the Flask Application
1. While inside the project's root directory and with the virtual environment activated, run the following command:

```bash
python app.py
```

2. You should see a message indicating that the server has started, usually with a URL like http://127.0.0.1:5000/.
3. Open the provided URL in your web browser to view and interact with the Flask application!

That's it! You've successfully set up and run the HitTheCodeLabs Website project locally. Don't forget to check out the [**live demo!**](https://gpt-curriculum-info-extractor.uc.r.appspot.com/) Enjoy exploring and customizing further!
