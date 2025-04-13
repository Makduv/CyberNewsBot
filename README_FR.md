# 🤖 CyberNews Discord Bot

Un bot Discord qui récupère les derniers articles de **The Hacker News**, propose une sélection, et génère automatiquement un **résumé en moins de 1800 caractères** grâce à l'API **ChatGPT (GPT-3.5)**.

---

## 🔧 Fonctionnalités

- 📥 Scraping des articles récents de [thehackernews.com](https://thehackernews.com)
- 📜 Interaction utilisateur via Discord (`$news`)
- ✍️ Résumé automatique par **GPT-3.5 Turbo**
- 🤖 Utilisation de `discord.py`, `BeautifulSoup`, `OpenAI`, etc.

---

## ⚙️ Prérequis

- Python ≥ 3.8  
- Clé API OpenAI  
- Token de bot Discord  
- Un terminal sur **Mac/Linux/Windows**  
- Git (optionnel)

---

## 📦 Installation

1. **Clone du projet**  
```bash
git clone https://github.com/ton-utilisateur/nom-du-projet.git
cd nom-du-projet
```

2. **Création d’un environnement virtuel**
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Mac/Linux
# .\venv\Scripts\activate  (Windows)
```

3. **Installation des dépendances**
```bash
pip install -r requirements.txt
```

---

## 📁 Fichier `.env` requis

Crée un fichier `.env` à la racine du projet avec ces deux lignes :

```
DISCORD_TOKEN=ton_token_discord
OPENAI_API_KEY=ta_cle_api_openai
```

Tu peux créer un bot sur [Discord Developer Portal](https://discord.com/developers/applications)  
Et générer une clé OpenAI ici : [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

---

## 🧪 Lancer le projet (Mac / Linux)

```bash
source venv/bin/activate
python3 ton_script.py
```

(Si ton fichier s’appelle `bot.py`, adapte à `python3 bot.py`)

---

## 🧰 Dépendances

Fichier `requirements.txt` recommandé :

```txt
discord.py
requests
beautifulsoup4
openai
python-dotenv
```

Pour le créer automatiquement :

```bash
pip freeze > requirements.txt
```

---

## 🧠 Exemple d’utilisation

1. Tape `$news` dans un salon Discord
2. Le bot te propose une liste des 12 derniers articles
3. Réponds avec un numéro (ex : `3`)
4. GPT-3.5 lit l’article, le résume, et t’envoie une synthèse lisible dans Discord

---

## 🛡️ Sécurité

- Les clés API sont stockées dans `.env` (ne jamais commit ce fichier)
- Utilise `.gitignore` avec :
```
.venv/
.env
__pycache__/
```

---

## 📚 Crédits

- [The Hacker News](https://thehackernews.com)
- [OpenAI API](https://platform.openai.com/docs/)
- [discord.py](https://discordpy.readthedocs.io)
