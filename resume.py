import discord
from discord.ext import commands
import youtube_dl

class Resume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix="!")
    musics = {}
    ytdl = youtube_dl.YoutubeDL()
    
    @bot.command()
    async def resume(self, ctx):
        client = ctx.guild.voice_client
        if client.is_paused():
            print("resume")
            client.resume()


