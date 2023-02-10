# MESSAGE_CONTENT intent required

import discord
import random

import modules.topics as topics

intents = discord.Intents(messages=True)
client = discord.Client(intents=intents)

prefix = "-"
version = "0.1.0"     # do not change

print(f"###############################")
print(f"# engineer v{version}             #")
print(f"# authored by sudokoko        #")
print(f"###############################\n")

clientToken = input("<Engineer> [DiscordBot:Main] Please specify the API token for the bot or press ENTER to use ENV: ")

def log(source: str, info: str):
    print(f'<Engineer> [{source}:Main] {info}')

@client.event
async def on_ready():
    log("DiscordBot", f"Logged in as {client.user}")


###############################
# TOPICS COMMAND              #
#  - {prefix}topic            #
#  - prints a conversation    #
#    starter or topic         #
###############################

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == f'{prefix}topic':
        randomTopic = random.choice(topics.topics)

        log("Topics", f"Topic selected from array: {randomTopic}")
        await message.channel.send(f'{randomTopic}')

###############################


client.run(clientToken)