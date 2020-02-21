import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('.help for commands list!'))
    print("I am ready!")

@client.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    
    embed.set_author(name='<<< COMMANDS LIST >>>')
    embed.add_field(name='Moderation:', value='===============', inline=False)
    embed.add_field(name='.ban = Ban a Member', value='---------------', inline=False)
    embed.add_field(name='.kick = Kick a Member', value='---------------', inline=False)
    embed.add_field(name='.clear = Clear Messages', value='---------------', inline=False)
    embed.add_field(name='.mute = Mute a Member', value='---------------', inline=False)
    embed.add_field(name='.unmute = Unmute a Muted Member', value='---------------', inline=False)
    embed.add_field(name='Fun:', value='===============', inline=False)
    embed.add_field(name='.ping', value= 'Best Admin Bot', inline=False)

    await ctx.author.send(author, embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f"You have {round(client.latency * 1000)}ms")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send('{} kicked by {}' .format(member.mention, ctx.author.mention))

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send('{} banned by {}' .format(member.mention, ctx.author.mention))

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(mute_members=True)
async def mute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            await ctx.send("{} has been muted by {}." .format(member.mention, ctx.author.mention))
            return

            overwrite = discord.PermissionOverwrite(send_messages=False)
            newRole = await guild.create_role(name="Muted")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole, overwrite=overwrite)

            await member.add_role(newRole)
            await ctx.send("{} has been muted by {}." .format(member.mention, ctx.author.mention))

@client.command()
@commands.has_permissions(mute_members=True)
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send ("{} has been unmuted by {}." .format(member.mention, ctx.author.mention))
            return

client.run('Njc5MjYzOTA3Njg4MjE4NjI0.Xk1XGw.WkNPSneGbYsdoR2a4VaZYeCWA90')