from time import ctime
import discord
from discord.ext import commands
import youtube_dl

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix="!")
    musics = {}
    ytdl = youtube_dl.YoutubeDL()

#Ban   
    @bot.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user : discord.User, *, reason = "Aucune raison n'a été donnée"):
        print("ban")
        await ctx.guild.ban(user, reason = reason)
        embed = discord.Embed(title = "__**Banissement**__", description = "Un modérateur a frappé !", color = 0xc3c1c1)
        embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/BanneHammer.png")
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.add_field(name = "Membre ban", value = user.name, inline = False)
        embed.add_field(name = "Raison", value = reason, inline = True)
        embed.add_field(name = "Staff", value = ctx.author.name, inline = True)

        await ctx.send(embed = embed)

#Unban
    @bot.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, user, *, reason = "Aucune raison n'a été donnée"):
        print("unban")
        userName, userId = user.split("#")
        bannedUsers = await ctx.guild.bans()
        for i in bannedUsers:
            if i.user.name == userName and i.user.discriminator == userId:
                await ctx.guild.unban(i.user, reason =  reason)
                embed = discord.Embed(title = "__**Banissement**__", description = "Un modérateur a frappé !", color = 0xc3c1c1)
                embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/BanneHammer.png")
                embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                embed.add_field(name = "Membre unban", value = f"{user} à été unban pour la raison suivante : {reason}.", inline = False)

                await ctx.send(embed = embed)
                return
        await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")

#Liste des bans
    @bot.command()
    @commands.has_permissions(ban_members = True)
    async def banid(self, ctx):
        print("banid")
        ids = []
        bans = await ctx.guild.bans()
        for i in bans:
            ids.append(str(i.user.id))
        await ctx.send("La liste des id des utilisateurs bannis du server est :")
        await ctx.send("\n".join(ids))

#unmute
    @bot.command()
    @commands.has_permissions(ban_members = True)
    async def unmute(self, ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
        print("unmute")
        mutedRole = await getMutedRole(ctx)
        await member.remove_roles(mutedRole, reason = reason)
        await ctx.send(f"{member.mention} a été unmute !")

#kick
    @bot.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user : discord.User, *reason):
    	reason = " ".join(reason)
    	await ctx.guild.kick(user, reason = reason)
    	await ctx.send(f"{user} à été kick.")

#clear
    @bot.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, nombre : int):
        print("clear")
        messages = await ctx.channel.history(limit = nombre + 1).flatten()
        for message in messages:
            await message.delete()

#mute
    @bot.command()
    @commands.has_permissions(ban_members = True)
    async def mute(self, ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
        print("mute")
        mutedRole = await getMutedRole(ctx)
        await member.add_roles(mutedRole, reason = reason)
        await ctx.send(f"{member.mention} a été mute !")

async def createMutedRole(self, ctx):
    mutedRole = await ctx.guild.create_role(name = "Mute",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Mute pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole

async def getMutedRole(self, ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Mute":
            return role
    return await createMutedRole(ctx)



