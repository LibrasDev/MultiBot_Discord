import discord
from discord.ext import commands
from discord.ext import tasks
import youtube_dl
import asyncio
import random

import stop
import skip
import resume
import pause
import helpCommands
import moderation

bot = commands.Bot(command_prefix="!", description = "Music Bot")
musics = {}
ytdl = youtube_dl.YoutubeDL()
status = ["!commands",
		"A votre service",
		"La terre est ronde",
		"La moitié de 2 est 1",
        "1 = 1;",
		"Pourquoi lisez-vous ca ?"]

#Status
@bot.event
async def on_ready():
    print("Ready !")

@bot.event
async def on_ready():
	print("Ready !")
	changeStatus.start()

@bot.command()
async def start(ctx, secondes = 5):
	changeStatus.change_interval(seconds = secondes)

@tasks.loop(seconds = 5)
async def changeStatus():
	game = discord.Game(random.choice(status))
	await bot.change_presence(status = discord.Status.mro, activity = game)

#Play
class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
        , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)


    client.play(source, after=next)

@bot.command()
async def play(ctx, url):
    print("play")
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        play_song(client, musics[ctx.guild], video)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):        
		await ctx.send("Cette commande n'existe pas.")
	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Il manque un argument.")
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send("Vous n'avez pas les permissions pour faire cette commande.")
	elif isinstance(error.original, discord.Forbidden):
		await ctx.send("Je n'ai pas les permissions nécéssaires pour faire cette commmande")

bot.add_cog(stop.Stop(bot))
bot.add_cog(skip.Skip(bot))
bot.add_cog(resume.Resume(bot))
bot.add_cog(pause.Pause(bot))
bot.add_cog(helpCommands.Help(bot))
bot.add_cog(moderation.Moderation(bot))

bot.run("NzQwNjYwMjIyMTUzOTgyMDUz.XysPlQ.rwrSVCLLTNdIcmShKS6sWI2qtfY")