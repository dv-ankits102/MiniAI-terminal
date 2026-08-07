# 🤖 MiniAI Terminal

A lightweight AI-powered terminal assistant built with Python. MiniAI allows users to chat with a local AI model, search the web, and manage conversation history directly from the command line.

---

## ✨ Features

- 💬 AI Chat using Ollama
- 🌐 Web Search using DDGS
- 📝 Conversation History
- 🧹 Clear Chat Memory
- ⚡ Fast Terminal Interface
- 🏗️ Modular Project Structure
- 🔌 Easy to Extend

---

## 📸 Preview

```bash
[You] /chat What is Python?

🤖 Python is a high-level programming language...
```

---

## 📂 Project Structure

```
MiniAI-terminal/
│
├── commands/
├── config/
├── core/
├── providers/
├── services/
├── app.py
├── router.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/dv-ankits102/MiniAI-terminal.git
cd MiniAI-terminal
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download and install Ollama from:

https://ollama.com

Pull a model:

```bash
ollama pull llama3.2:3b
```

Run Ollama:

```bash
ollama serve
```

---

## ▶️ Run

```bash
python main.py
```

---

## 📌 Commands

| Command | Description |
|----------|-------------|
| `/chat <question>` | Chat with AI |
| `/search <query>` | Search the web |
| `/history` | Show chat history |
| `/clear` | Clear conversation |
| `/help` | Show help |
| `/exit` | Exit MiniAI |

---

## 🛠️ Tech Stack

- Python
- Ollama
- Requests
- Rich
- DDGS

---

## 🎯 Future Roadmap

- Multi AI Provider Support
- Voice Chat
- PDF Reader
- Image Understanding
- Plugin System
- Better Memory
- RAG Support

---

## 👨‍💻 Author

**Honey Kumar**

GitHub:
https://github.com/dv-ankits102

---

⭐ If you like this project, please give it a Star.
