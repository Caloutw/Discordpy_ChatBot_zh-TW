import discord
import Process_Output

Creator = "HaroiiiX3 / 羽晴"
BotName = ["Haroi_ChatV10"]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == self.user:
            return
        for i in BotName:
            if message.content.startswith(i):
                process_message = message.content[len(i):].strip()
                await message.channel.send(Process_Output.Chat_Program(process_message,i, Creator))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')