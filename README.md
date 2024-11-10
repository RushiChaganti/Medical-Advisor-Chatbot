# Medical-Advisor-Chatbot
## Medical Advisor Chatbot - Combined Readme

### Overview

This project encompasses two versions of a medical advisor chatbot: one as a Streamlit web application and the other as a Telegram bot. Both versions utilize Ollama's AI model to provide health-related advice to users.

## Features

### Streamlit Web App
- **Health-related chatbot**: Users can ask questions about symptoms, stress management, and other health-related topics.
- **Real-time interactions**: Immediate responses based on the model's knowledge.
- **Streamlit frontend**: A user-friendly web interface for asking questions and viewing answers.
- **Message history**: Displays the conversation between the user and the assistant[1].

### Telegram Bot
- **Responds to user queries**: Provides health-related information in response to user questions.
- **Retry logic**: Includes retry logic for both Ollama API requests and Telegram message sending.
- **Welcome and help commands**: `/start` for a welcome message and `/help` for usage instructions[1].

## Requirements

### Common Requirements
- **Python 3.8 or higher**: Necessary for running both the Streamlit app and the Telegram bot.
- **Ollama running locally**: The Ollama API must be running at `http://localhost:11434` for both versions.

### Streamlit Web App
- **Streamlit library**
- **requests**: For making HTTP requests to the Ollama API.
- **ollama**: For interacting with Ollama's AI model.
- **Necessary Python packages**:
  ```
  requests==2.28.1
  ollama==0.2.0
  streamlit==1.20.0
  ```

### Telegram Bot
- **Telegram Bot Token**: Generated via BotFather.
- **python-dotenv**: To load environment variables.
- **loguru**: For logging purposes.
- **telegram and telegram-ext**: For interacting with the Telegram Bot API.
- **Necessary Python packages**:
  ```
  requests
  python-dotenv
  ollama
  loguru
  telegram
  telegram-ext
  ```

## Setup Instructions

### Streamlit Web App

#### Step 1: Clone the Repository
```
git clone "https://github.com/RushiChaganti/Medical-Advisor-Chatbot.git"
cd .\Medical-Advisor-Chatbot\
```

#### Step 2: Create a Virtual Environment
For **Windows**:
```bash
python -m venv myenv
myenv\Scripts\activate
```
For **Linux/Mac**:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

#### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Set Up Environment Variables
Ensure Ollama is running locally:
```bash
python -m ollama.server
```

#### Step 5: Run the Streamlit App
```bash
streamlit run app.py
```

### Telegram Bot

#### Step 1: Clone the Repository
```bash
git clone <repository_url>
cd <repository_name>
```

#### Step 2: Create a Virtual Environment
For **Windows**:
```bash
python -m venv myenv
myenv\Scripts\activate
```
For **Linux/Mac**:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

#### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Set Up Environment Variables
Create a `.env` file with:
```
TELEGRAM_BOT_TOKEN=<your-telegram-bot-token>
```

#### Step 5: Install and Run Ollama API
Ensure Ollama is running locally:
```bash
python -m ollama.server
```

#### Step 6: Run the Bot
```bash
python bot.py
```

## Usage

### Streamlit Web App
- **Ask a Question**: Type a health-related question in the input field and click "Ask" to get a response.
- **Message History**: View the previous conversation displayed on the screen.
- **Start Over**: Click the "Start Over" button to clear the chat history.

### Telegram Bot
- **/start**: A welcome message for first-time users.
- **/help**: A message with information on how to use the bot.
- **User Message**: Ask a health-related question, and the bot will respond with relevant information.

## Troubleshooting

### Streamlit Web App
- **Ollama API not running**: Ensure Ollama is running at `http://localhost:11434`.
- **Streamlit app not opening**: Check for errors in the terminal and ensure the app is running at `http://localhost:8501`.
- **Network Issues**: Check your network connection and firewall settings.

### Telegram Bot
- **Connection error**: Ensure the Ollama server is running on the correct port (`http://localhost:11434`).
- **Message sending issues**: Check your network connection and ensure the `TELEGRAM_BOT_TOKEN` is correct.

## License

Both projects are licensed under the MIT License.