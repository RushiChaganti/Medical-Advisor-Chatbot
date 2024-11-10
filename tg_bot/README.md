---

# Medical Advisor Chatbot - Telegram Bot

This is a Telegram bot that uses Ollama's API to provide health-related advice to users. The bot can answer questions about medical conditions, symptoms, stress management, and more.

## Features

- Responds to user queries with health-related information.
- Includes retry logic for both Ollama API requests and Telegram message sending.
- A welcoming `/start` command for first-time users.
- `/help` command to assist users with bot usage.

## Requirements

To run this project, you need the following:

- Python 3.8+ (preferably a virtual environment)
- Telegram Bot Token (generated via BotFather)
- Ollama running locally (http://localhost:11434)
  
### Required Python packages:

- `requests`: For making HTTP requests.
- `python-dotenv`: To load environment variables.
- `ollama`: To communicate with Ollama API.
- `loguru`: For logging purposes.
- `telegram`: For interacting with the Telegram Bot API.
- `telegram-ext`: For Telegram bot framework utilities.

---

## Setup Instructions

### Step 1: Clone the Repository

Clone the repository to your local machine:

```
git clone "https://github.com/RushiChaganti/Medical-Advisor-Chatbot.git"
cd .\Medical-Advisor-Chatbot\
```

### Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to isolate your project dependencies.

1. **Create the virtual environment:**

   For **Windows**:

   ```bash
   python -m venv myenv
   ```

   For **Linux/Mac**:

   ```bash
   python3 -m venv myenv
   ```

2. **Activate the virtual environment:**

   For **Windows**:

   ```bash
   myenv\Scripts\activate
   ```

   For **Linux/Mac**:

   ```bash
   source myenv/bin/activate
   ```

### Step 3: Install Required Dependencies

With the virtual environment activated, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory of your project with the following content:

```
TELEGRAM_BOT_TOKEN=<your-telegram-bot-token>
```

- Replace `<your-telegram-bot-token>` with the token you receive from the [BotFather](https://core.telegram.org/bots#botfather) when you create your Telegram bot.

### Step 5: Install and Run Ollama API

Ensure that the Ollama service is running locally. You can either use the local Ollama API or configure it according to your setup.

1. **Start the Ollama API server**:

   ```bash
   python -m ollama.server
   ```

2. **Make sure the Ollama server is available at `http://localhost:11434`.**

### Step 6: Run the Bot

Once all dependencies are installed and your environment is set up, you can run the bot with:

```bash
python bot.py
```

The bot will start running and will be able to respond to user queries via Telegram.

---

## Usage

- **/start**: A welcome message for first-time users.
- **/help**: A message with information on how to use the bot.
- **User Message**: Ask a health-related question, and the bot will respond with relevant information from Ollama.

---

## Troubleshooting

- If you encounter a **connection error** when the bot tries to reach Ollama, ensure that the Ollama server is running on the correct port (`http://localhost:11434`).
- If you experience issues with sending messages via the Telegram Bot API, check your network connection and ensure that your `TELEGRAM_BOT_TOKEN` is correct.

---

## License

This project is licensed under the MIT License.

---
