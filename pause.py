from time import ctime
import discord
from discord.ext import commands
import youtube_dl

class Pause(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix="!")
    musics = {}
    ytdl = youtube_dl.YoutubeDL()
    
    @bot.command()
    async def pause(self, ctx):
        client = ctx.guild.voice_client
        if not client.is_paused():
            print("pause")
            client.pause()
