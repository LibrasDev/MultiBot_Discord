from re import purge
import discord
from discord.ext import commands
import youtube_dl

musics = {}

class Stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix="!")
    ytdl = youtube_dl.YoutubeDL()
    
    @bot.command()
    async def stop(self, ctx):
        client = ctx.guild.voice_client
        await client.disconnect()
        print("stop")
        musics[ctx.guild] = []


