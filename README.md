# 🤖 CyberNews Discord Bot

A Discord bot that fetches the latest articles from **The Hacker News**, offers a selection, and automatically generates a **summary under 1800 characters** using the **ChatGPT (GPT-3.5)** API.

---

## 🔧 Features

- 📥 Scrapes recent articles from [thehackernews.com](https://thehackernews.com)  
- 📜 User interaction via Discord (`$news` command)  
- ✍️ Auto-summary using **GPT-3.5 Turbo**  
- 🤖 Uses `discord.py`, `BeautifulSoup`, `OpenAI`, and more

---

## ⚙️ Requirements

- Python ≥ 3.8  
- OpenAI API Key  
- Discord Bot Token  
- Terminal (Mac/Linux/Windows)  
- Git (optional)

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/project-name.git
cd project-name
```

2. **Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
# .\venv\Scripts\activate  (Windows)
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 📁 Required `.env` File

Create a `.env` file at the root of the project with these two lines:

```
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
```

You can create a bot at [Discord Developer Portal](https://discord.com/developers/applications)  
And generate an API key here: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

---

## 🧪 Run the project (Mac / Linux)

```bash
source venv/bin/activate
python3 your_script.py
```

(If your file is named `bot.py`, run `python3 bot.py`)

---

## 🧰 Dependencies

Recommended `requirements.txt`:

```txt
discord.py
requests
beautifulsoup4
openai
python-dotenv
```

To generate it automatically:

```bash
pip freeze > requirements.txt
```

---

## 🧠 How to use

1. Type `$news` in a Discord channel  
2. The bot will display the 12 most recent articles  
3. Reply with a number (e.g., `3`)  
4. GPT-3.5 will read the article, summarize it, and send it back as a readable Discord message

---

## 🛡️ Security

- API keys are stored in `.env` (⚠️ never commit this file)
- Use a `.gitignore` like:

```
.venv/
.env
__pycache__/
```

---

## 📚 Credits

- [The Hacker News](https://thehackernews.com)  
- [OpenAI API](https://platform.openai.com/docs/)  
- [discord.py](https://discordpy.readthedocs.io)
