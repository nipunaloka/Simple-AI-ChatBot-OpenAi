# AI Terminal Chatbot using OpenRouter & Python

A simple AI-powered terminal chatbot built with Python, OpenRouter API, and the OpenAI SDK.  
This project allows users to interact with AI models directly from the command line in real time.

---

## Features

- Real-time AI conversation in terminal
- Uses OpenRouter API with OpenAI SDK
- Environment variable support using `.env`
- Configurable AI model and parameters
- Lightweight and beginner-friendly project

---

## Technologies Used

- Python
- OpenAI Python SDK
- OpenRouter API
- python-dotenv

---

## Project Structure

```bash
project/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2. Navigate to Project Folder

```bash
cd your-repository-name
```

### 3. Create Virtual Environment

```bash
python -m virtualenv env
```

### 4. Activate Virtual Environment

#### Windows

```bash
env\Scripts\activate
```

#### Mac/Linux

```bash
source env/bin/activate
```

### 5. Install Dependencies

```bash
pip install openai python-dotenv
```

---

## Environment Variables

Create a `.env` file in the root directory.

```env
OPEN_API_KEY=your_openrouter_api_key
```

Get your API key from:

https://openrouter.ai/

---

## Run the Application

```bash
python app.py
```

---

## Example

```bash
User: Hello
AI: Hello! How can I help you today?
```

Type:

```bash
exit
```

to stop the chatbot.

---

## Code Overview

### AI Model Configuration

```python
model="openai/gpt-3.5-turbo"
```

### Parameters Used

| Parameter | Description |
|---|---|
| max_tokens | Maximum response length |
| temperature | Controls randomness |
| n | Number of responses |

---

## Future Improvements

- GUI interface
- Streamlit web app
- Voice assistant integration
- Chat history support
- Multiple AI model selection
- AI agent features

---

## Learning Objectives

This project helps beginners understand:

- API integration
- AI chatbot development
- Environment variables
- Python virtual environments
- Working with LLMs

---

## Author

Nipun Bandara

- GitHub: https://github.com/nipunaloka
- LinkedIn: https://linkedin.com/in/nipun-bandara-b28a93201

---
