# MESSAGE_CONTENT intent required

import discord
import os
import random

import modules.topics as topics

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

prefix = "-"

def log(source: str, info: str):
    print(f'<Engineer> [{source}:Main] {info}')

@client.event
async def on_ready():
    log("DiscordBot", f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == f'{prefix}topic':
        randomTopic = random.choice(topics.topics)

        log("Topics", f"Topic selected from array: {randomTopic}")
        await message.channel.send(f'{randomTopic}')

client.run(os.environ.get('DISCORD_BOT_TOKEN'))