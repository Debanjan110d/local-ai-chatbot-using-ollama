

# Local AI Chatbot Using Ollama

This is an interactive chatbot built using Python, LangChain, and the Ollama LLM with the Llama 3 model. The chatbot maintains a context-aware conversation with users and can answer a wide range of questions.

---

## Features

- **Context Awareness**: The chatbot remembers previous inputs for more natural conversations.
- **Powered by Ollama LLM**: Utilizes the Llama 3 model for intelligent responses.
- **Simple to Use**: Easy setup and operation in your local environment.

---

## Installation and Setup

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/Debanjan-dev/Local-ai-Chatbot-using-Ollama-
cd Local-ai-Chatbot-using-Ollama-
```


### 2. Set Up a Python Virtual Environment
Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 4. Install Ollama and Llama 3 Model
To use this chatbot, you need to install the Ollama software and download the Llama 3 model.

#### Step 4.1: Download Ollama
Visit the [Ollama website](https://ollama.ai/) and download the software for your operating system. Follow the installation instructions provided on their site.

#### Step 4.2: Set Up the Llama 3 Model
After installing Ollama, download the Llama 3 model:
```bash
ollama pull llama3
```

---

## Usage

### 1. Start the Chatbot
Run the chatbot by executing the `main.py` file:
```bash
python main.py
```

### 2. Chat With the Bot
Once the chatbot starts, you can type your questions in the terminal. For example:
```text
You: What is the capital of France?
Chatbot: The capital of France is Paris.
```

To end the conversation, type:
```text
You: quit
```

---

## Project Structure

```
Local-ai-Chatbot-using-Ollama-
│
├── main.py               # Main Python script for the chatbot
├── requirements.txt      # List of Python dependencies
└── README.md             # Documentation
```

---

## How It Works

1. **Conversation Template**: A custom template is defined to manage conversation context.
2. **LangChain Integration**: LangChain connects the chatbot prompt with the Llama 3 model.
3. **Ollama LLM**: The Llama 3 model processes the input and generates intelligent responses.
4. **Interactive Terminal**: The chatbot interacts with users through the terminal, maintaining context across exchanges.

---

## Example Conversation
```text
Welcome to the chatbot!
You: What is Python?
Chatbot: Python is a high-level programming language known for its simplicity and versatility.
You: Who created Python?
Chatbot: Python was created by Guido van Rossum in 1991.
You: quit
```

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

### Author
**Debanjan Dutta**  
GitHub: [Debanjan-dev](https://github.com/Debanjan-dev)
#
