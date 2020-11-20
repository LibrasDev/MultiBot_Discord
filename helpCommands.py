from time import ctime
import discord
from discord.ext import commands
import youtube_dl


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix="!")
    musics = {}
    ytdl = youtube_dl.YoutubeDL()
    
    @bot.command()
    async def commands(self, ctx):
        print("Commands")
        embed = discord.Embed(title = "__**Musique**__", color = 0xc3c1c1)
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.add_field(name = "!play {url}", value = "Lancer une musique", inline = False)
        embed.add_field(name = "!pause", value = "Mettre la musique sur pause", inline = False)
        embed.add_field(name = "!resume", value = "Relancer la musique", inline = False)
        embed.add_field(name = "!skip", value = "Passer la musique", inline = False)
        embed.add_field(name = "!stop", value = "Stopper la musique", inline = False)

        await ctx.send(embed = embed)
        
        embed = discord.Embed(title = "__**Modération**__", color = 0xc3c1c1)
        embed.add_field(name = "!ban {pseudo} {raison}", value = "Ban une personne", inline = False)
        embed.add_field(name = "!unban {pseudo#0000} {raison}", value = "Unban une personne **Attention** le pseudo doit être écrit en entier avec le #", inline = False)
        embed.add_field(name = "!banid", value = "Liste des bans", inline = False)
        embed.add_field(name = "!mute {pseudo} {raison}", value = "Mute une personne", inline = False)
        embed.add_field(name = "!unmute {pseudo} {raison} ", value = "Unmute Une personne", inline = False)
        embed.add_field(name = "!kick {pseudo} {raison}", value = "Kick une personne", inline = False)
        embed.add_field(name = "!clear {Nombre_De_Message}", value = "Supprimer un nombre de message défini", inline = False)

        await ctx.send(embed = embed)
