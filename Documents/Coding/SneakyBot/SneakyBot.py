import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await self.change_presence(activity=discord.Streaming(name="With LiftsFromRBLX!", url='https://www.twitch.tv/liftsfromroblox'))

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == client.user:
            return

        if message.content == 'S/help':
            await message.channel.send('Documentation for SneakyBot!')
            await message.channel.send('`Hello i am SneakyBot! I use discord.py Anyways commands are Coming Soon™️`')
            
        if message.content == 'S/ban @GenericLover12345 shut up nobody likes generics F':
            await message.channel.send(f'Task Succesfull, {message.author}.')
            await message.channel.send('Banned GenericLover12345 Forever!')
         
        
        if message.content == 'S/greet':
            await message.channel.send('Hello I am SneakyBot! An Advanced bot made by Sneaky#6542. I use Discord.py [insert coughing here] I only know Python and Lua so Python it is lol. Here is my Invite! https://discord.com/api/oauth2/authorize?client_id=741153070095794186&permissions=8&scope=bot')
            
        if message.content == 'S/unload':
            await message.channel.send(f'{message.author}, **SHUTTING THE BOT DOWN ON ALL SERVERS')
            exit()

client = MyClient()
client.run(os.environ['TOKEN_FOR_BOT'])