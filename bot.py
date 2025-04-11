import discord
from dotenv import load_dotenv
import os
import requests #Permet de faire des requêtes HTTP
from bs4 import BeautifulSoup
from openai import OpenAI
import asyncio


#Charger les clés de façon sécurisé
load_dotenv()
GPT = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

######ChatGPT : Une fois l'article choisi on donne son texte a GPT qui va faire un résumé.
async def gpt_resume(article_content: str) -> str:

    #Défini le bot
    system_msg = (
        "Tu es un super assistant expert en cybersécurité et en rédaction journalistique."
    )
    #Message qu'on lui envoi
    user_msg = (
        "Fais-moi un résumé de 1800 caractères maximum, titre compris, sur l'article ci-dessous. "
        "Le résumé ne doit **jamais** dépasser cette limite sinon il sera bloqué par Discord.\n\n"
        + article_content
    )
    
    #Création d'un dataset avec GPT
    response = GPT.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

###### Bot
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.lower() == "$news":
            await self.find_article(message)

    async def find_article(self, message):

        #On accède à la page/code HTML du site
        page = requests.get('https://thehackernews.com/', headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        #On recupère les URLs des articles
        articles = soup.find_all(class_='story-link')
        urls = [a["href"] for a in articles if a.has_attr("href")]
        
        #On récupère les titres de chaque article
        articles_titles = soup.find_all(class_='home-title')
        titles = [tag.get_text(strip=True) for tag in articles_titles]

        # Envoi de la liste à l'utilisateur
        msg = "**📰 Articles récents :**\n\n"
        for i, title in enumerate(titles, start=1):
            msg += f"{i}) {title}\n"
        msg += "\n➡️ Tape le numéro de l'article qui t'intéresse :"
        await message.channel.send(msg)

        # Attente de la réponse de l'utilisateur
        def check(m): #On verifie que l'entré est bonne
            return m.author == message.author and m.channel == message.channel and m.content.isdigit() and 1 <= int(m.content) <= 12

        try:
            reply = await self.wait_for("message", timeout=30.0, check=check)
            choix = int(reply.content)
            url_choisi = urls[choix - 1]

            # Récupération du contenu de l’article
            page = requests.get(url_choisi, headers=headers)
            soup = BeautifulSoup(page.text, 'html.parser')
            article_title = soup.find('title').get_text(strip=True)
            article_content = soup.find('div', class_='articlebody clear cf')
            text = " ".join(p.get_text(strip=True) for p in article_content.find_all('p'))

            await message.channel.send("✍️ Je résume l’article avec GPT, un instant...\n")

            try:
                summary = await gpt_resume(text)
                await message.channel.send(summary)
                
            except Exception as e:
                await message.channel.send(f"❌ Erreur pendant le résumé : {e}")

        except asyncio.TimeoutError:
            await message.channel.send("⏳ Temps écoulé.")

        except Exception as e:
            await message.channel.send(f"❌ Une erreur est survenue : {e}")
            

#Lance le bot
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))
