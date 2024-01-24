import discord
import Process_Output

Creator = "Haroiii"
BotName = ["雨晴","YQ","x6","x6n","X6","X6N"]

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
                await message.reply(Process_Output.Chat_Program(process_message,i, Creator))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE2NjI2MjE5MTY5MTkyMzQ3OA.GuHsjq.T2edDo4Ddb8jR2c1EBY4EL7JVnO3lmfHmuUEWM')