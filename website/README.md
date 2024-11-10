---

# Medical Advisor Chatbot - Streamlit Web App

This is a **Streamlit-based web application** that provides health-related advice using Ollama's AI model. The chatbot can answer questions related to symptoms, health management, and other medical inquiries. 

## Features

- **Health-related chatbot**: Ask the bot questions about symptoms, stress management, and other health-related topics.
- **Real-time interactions**: Receive immediate responses based on the model's knowledge.
- **Streamlit frontend**: The app provides a user-friendly web interface for users to ask questions and view answers.
- **Message history**: Displays the conversation between the user and the assistant.

## Requirements

- Python 3.8 or higher
- Ollama running locally at `http://localhost:11434`
- Streamlit library
- Necessary Python packages

### Required Python packages:

- `requests`: For making HTTP requests to Ollama API.
- `ollama`: For interacting with Ollama's AI model.
- `streamlit`: For creating the web interface.
  
---

## Setup Instructions

### Step 1: Clone the Repository

Clone the repository to your local machine:

```
git clone "https://github.com/RushiChaganti/Medical-Advisor-Chatbot.git"
cd .\Medical-Advisor-Chatbot\
```

### Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

1. **Create the virtual environment**:

   For **Windows**:

   ```bash
   python -m venv myenv
   ```

   For **Linux/Mac**:

   ```bash
   python3 -m venv myenv
   ```

2. **Activate the virtual environment**:

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

Make sure Ollama is running locally on your machine. You can either use the pre-configured Ollama API server or set it up as per your configuration.

1. **Start Ollama server**:

   Run the following command to start the Ollama API locally (ensure the server is running on `http://localhost:11434`):

   ```bash
   python -m ollama.server
   ```

2. **Make sure the server is running**: You can check if the Ollama API is working by visiting `http://localhost:11434` in your browser or via a `GET` request.

### Step 5: Run the Streamlit App

Once the dependencies are installed and your environment is set up, run the app with:

```bash
streamlit run app.py
```

This will start the Streamlit app and provide a link (usually `http://localhost:8501`) where you can interact with the chatbot in your web browser.

---

## Usage

- **Ask a Question**: Type a health-related question in the input field and click "Ask" to get a response from the assistant.
- **Message History**: See the previous conversation displayed on the screen.
- **Start Over**: If you want to reset the conversation, click the "Start Over" button to clear the chat history.

---

## Requirements (`requirements.txt`)

The following are the necessary dependencies for this project:

```
requests==2.28.1
ollama==0.2.0
streamlit==1.20.0
```

---

## Troubleshooting

- **Ollama API not running**: Ensure that Ollama is running at `http://localhost:11434`. If not, start the server using `python -m ollama.server`.
- **Streamlit app not opening**: Make sure there are no errors in the terminal and the app is running at `http://localhost:8501`.
- **Network Issues**: If you're having trouble with connecting to the Ollama API or the Streamlit app, check your network connection and firewall settings.

---

## License

This project is licensed under the MIT License.

---

