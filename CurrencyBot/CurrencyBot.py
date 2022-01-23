import discord
from bs4 import BeautifulSoup
import requests

client = discord.Client()

@client.event

async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith("!Currency"):
        currency = message.content[10:].lower().replace(" ", "")
        url = f"https://coinmarketcap.com/currencies/{currency}/"

        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        try:
            Stock_Price = soup.find_all('span')[28].text
            await message.channel.send(currency.capitalize() + " Price: " + Stock_Price)
        except IndexError:
            await message.channel.send("Please use a valid currency")


client.run("TOKEN")
