import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

responses = {
    "こんにちは": "やあ、元気？",
    "おはよう": "おはよう！",
    "さようなら": "またね！",
}

@client.event
async def on_ready():
    print(f"ログイン成功: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content in responses:
        await message.channel.send(responses[message.content])

client.run(os.getenv("DISCORD_TOKEN"))
