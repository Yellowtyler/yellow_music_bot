import discord
import response_handler

async def send_message(message, user_message):
    try:
        response = response_handler.handle(message)
    except Exception as e:
        print(e)

def run_bot():
    TOKEN = ''
    client = discord.Client()
    
    @client.event
    async def on_ready():
        print('bot is running!')
        
    client.run(TOKEN)