import os
import sys
import requests
import time
from dotenv import load_dotenv
from ollama import Client
from loguru import logger
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.error import NetworkError, TelegramError

# Load environment variables
load_dotenv()

# Set up logging
logger.add("bot.log", level="INFO", rotation="1 MB", compression="zip")

# Ollama configuration
ollama_url = 'http://localhost:11434'

# Function to interact with Ollama's API with retry logic
def request(gpt_model, messages, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            logger.info(f"Attempt {attempt+1} to communicate with Ollama API.")
            response = client.chat(
                model=gpt_model,
                messages=[{"role": m["role"], "content": m["content"]} for m in messages],
                stream=True,
            )

            current_reply = ""
            for chunk in response:
                message = chunk['message']
                current_reply += message.get("content", "")
            return current_reply
        
        except (requests.exceptions.RequestException, requests.exceptions.ConnectionError) as e:
            logger.error(f"Network error occurred: {str(e)}. Retrying...")
            attempt += 1
            time.sleep(2)  # Wait before retrying
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}.")
            return "Sorry, something went wrong. Please try again later."

    return "Network is failing us. Please check your connection or try again later."

# Initialize the Ollama client
if requests.get(ollama_url).status_code == 200:
    client = Client(host=ollama_url)
else:
    logger.error("Ollama is not running")
    sys.exit(1)
async def retry_send_message(update, message, retries=3, delay=2):
    attempt = 0
    while attempt < retries:
        try:
            # Try sending the message
            await update.message.reply_text(message)
            return  # Exit after successful send
        except (NetworkError, TelegramError) as e:
            logger.error(f"Error sending message to Telegram: {str(e)}. Retrying...")
            attempt += 1
            time.sleep(delay)  # Wait before retrying
        except Exception as e:
            logger.error(f"Unexpected error while sending message: {str(e)}.")
            return  # Exit on unexpected error
    logger.error("Failed to send message after retries.")

# Handle /start command (send it only once)
async def start(update: Update, context):
    user_id = update.message.from_user.id
    # Check if this is the first time the user has interacted with the bot
    if 'start_done' not in context.user_data:
        context.user_data['start_done'] = True
        await update.message.reply_text(
            "🌟 Welcome to the Medical Advisor Chatbot! 🌟\n\n"
            "I am here to assist you with medical questions. Type any health-related question and I'll do my best to provide an answer.\n"
            "Use /help to learn more.\n\n"
            "💡 **Disclaimer**: This chatbot is not a substitute for professional medical advice. Always consult a healthcare provider before taking any medication."
        )
        logger.info(f"User {user_id} started the bot for the first time.")
    else:
        await update.message.reply_text("Welcome back! Feel free to ask any medical-related questions.")

# Handle /help command
async def help_command(update: Update, context):
    await update.message.reply_text(
        "This bot provides health-related advice based on your questions.\n\n"
        "Simply type your question, such as:\n"
        "- What are the symptoms of diabetes?\n"
        "- How can I manage stress?\n\n"
        "Note: This is not a substitute for professional medical advice. Always check with a professional before making health decisions."
    )
    logger.info(f"User {update.message.from_user.id} requested help.")

# Handle user messages
async def handle_message(update: Update, context):
    user_input = update.message.text
    user_id = update.message.from_user.id
    logger.info(f"Received message from {user_id}: {user_input}")

    if 'messages' not in context.user_data:
        context.user_data['messages'] = []

    # Add user message to the context
    context.user_data['messages'].append({"role": "user", "content": user_input})

    # Call the request function to get the bot's response with retry
    model_response = request("medllama2:7b", context.user_data['messages'])

    # Add the assistant's response to the context
    context.user_data['messages'].append({"role": "assistant", "content": model_response})

    # Retry sending the model's response to the user
    await retry_send_message(update, model_response)
    logger.info(f"Sent response to {user_id}: {model_response}")

# Main function to start the Telegram bot
def main():
    # Load the bot token from the environment variable
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        logger.error("Telegram bot token not found in .env file.")
        sys.exit(1)

    # Create the Application instance
    application = Application.builder().token(bot_token).build()

    # Add handlers for commands and messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()
    logger.info("Bot is now running...")

if __name__ == '__main__':
    main()
