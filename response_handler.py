import discord

async def handle(message):
    strs = message.split(' ')
    if strs[0] == 'play':
        if len(strs) == 1:
            return 'Please specify url'
        #valid url
        #get author's voice channel
        #connect to the channel
        #play music