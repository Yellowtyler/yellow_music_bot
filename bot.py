from discord.ext import commands
import discord
from discord import FFmpegPCMAudio
from pytube import YouTube
from os import path
import os
from api_key import TOKEN

def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.voice_states = True
    client = commands.Bot(command_prefix='', intents = intents)
    
    @client.event
    async def on_ready():
        print('bot is running!')

    @client.command(pass_context=True)
    async def join(ctx):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You must join voice channel!")
    
    @client.command(pass_context=True)
    async def leave(ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
        else:
            await ctx.send("You gotta be joined voice channel to leave!")

    @client.command(pass_context=True)
    async def play(ctx):
        if (not ctx.voice_client):
            await ctx.send("You gotta be joined voice channel to play music!")
        str_arr = str.split(ctx.message.content, ' ')
        print(str_arr)
        if (len(str_arr) == 1):
            await ctx.send("You need to add url to play your song!")
        url = str_arr[1]
        yt = YouTube(url)
        file = os.getcwd() + '\\' + yt.title + '.mp4'
        # issue with : in video title
        if (not path.exists(file)):
            file = yt.streams.filter(only_audio=True).order_by("abr").last().download()
        src = FFmpegPCMAudio(file)
        ctx.voice_client.play(src)
        await ctx.send("Playing song {}".format(url))

    @client.command(pass_context=True)
    async def pause(ctx):
        if (ctx.voice_client):
            voice_client = ctx.guild.voice_client
            if (voice_client.is_playing()):
                await voice_client.pause()
            else:
                await voice_client.resume()
        else:
            await ctx.send("You must join voice channel!")

    @client.command(pass_context=True)
    async def stop(ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.stop()
        else:
            await ctx.send("You must join voice channel!")

    client.run(TOKEN)