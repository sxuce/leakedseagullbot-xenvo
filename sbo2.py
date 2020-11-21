import discord
from discord.ext import commands
import json
import requests
client = commands.Bot(command_prefix = '.', case_insensitive=True)
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot online.")

@client.command()
async def genuser(ctx, usergened=None):
    if usergened == None:
        await ctx.send("Please provide a name as a base to create a username!")
    else:
        request = requests.get(f"http://www.crazyapi.tk/api-v1/RandomUsername.php?name={usergened}")
        await ctx.send(request.text)
@client.command()
async def randomlenny(ctx):
    request = requests.get("http://www.crazyapi.tk/api-v1/RandomLenny.php")
    await ctx.send(request.text)

@client.command()
async def insult(ctx, dissed : discord.Member=None):
    if dissed == None:
        request = requests.get("http://www.crazyapi.tk/api-v1/insult.php")
        await ctx.send(request.text) 
    else:
        request = requests.get("http://www.crazyapi.tk/api-v1/insult.php")
        await ctx.send(f"Hey! {dissed.mention} {request.text}")

@client.command()
async def tord(ctx, tordoption=None):
    if tordoption == None:
        await ctx.send("Hey! Please say truth or dare!")
    elif tordoption == "truth":
        request = requests.get("http://www.crazyapi.tk/api-v1/TruthOrDare.php?&Truth")
        await ctx.send(request.text)
    elif tordoption == "dare":
        request = requests.get("http://www.crazyapi.tk/api-v1/TruthOrDare.php?&Dare")
        await ctx.send(request.text)
    else:
        await ctx.send("Hey! Please **ONLY** do truth or dare.")     

@client.command()
async def btcprice(ctx, currencybtc=None):
    if currencybtc == None:
        await ctx.send("Hey! Please specify if you want it in `GBP` or `USD`, like this: `\".btcprice usd\"`")

    elif currencybtc.lower() == "gbp":
        requestgbp = requests.get("http://www.crazyapi.tk/api-v1/BitcoinPrice.php?gbp")
        await ctx.send(f"The current price for Bitcoin in GBP is : `£{requestgbp.text}`")

    elif currencybtc.lower() == "usd":
        requestusd = requests.get("http://www.crazyapi.tk/api-v1/BitcoinPrice.php?usd")
        await ctx.send(f"The current price for Bitcoin in USD is : `${requestusd.text}`")

    else:
        await ctx.send("Hey! Please only use `GBP` or `USD`.")

@client.command()
async def define(ctx, defword=None):
    if defword == None:
        await ctx.send("Hey! Please add a word to define!")
    else:
        request = requests.get(f"http://www.crazyapi.tk/api-v1/urbandic.php?word={defword}")
        await ctx.send(request.text)

@client.command()
async def covid(ctx, optioncovid=None):
    request = requests.get("https://api.thevirustracker.com/free-api?global=stats")
    packages_json = request.json()
    package_str = json.dumps(packages_json, indent=2)
    data = json.loads(package_str)
    if optioncovid == None:
        for results in data["results"]:
            await ctx.send(f"The current amount of `COVID-19` Cases are : `{(results['total_cases'])}`")
    elif optioncovid == "cases":
        for results in data["results"]:
            await ctx.send(f"The current amount of `COVID-19` Cases are : `{(results['total_cases'])}`")        
    elif optioncovid.lower() == "recovered":
        for results in data["results"]:
            await ctx.send(f"The current amount of people who recovered from `COVID-19` are : `{(results['total_recovered'])}`")
    elif optioncovid.lower() == "deaths":
        for results in data["results"]:
            await ctx.send(f"The current amount of `COVID-19` related deaths are : `{(results['total_deaths'])}`")

@client.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}! I am `Two Plus`. Your personal `information bot`!\nMy features have a wide range, from username makers (`genuser`) all the way to the amount of COVID-19 cases there are (`covid`)\nPlease contact `sauce#6190` `(feel free to friend me)` for support, bugs or suggestions!")

@client.command()
async def help(ctx, helpmore=None):
    if helpmore == None:
        embed=discord.Embed(
            title="TwoPlus Help Centre",
            color=0x00fffb
        )
        embed.add_field(name="Information :newspaper:", value=f"info\nhello")
        embed.add_field(name="Fun :rofl:", value=f"insult\nrandomlenny", inline=False)
        embed.add_field(name="Useful :face_with_monocle:", value=f"btcprice\ngenuser\ncovid", inline=False)
        embed.set_footer(text="TwoPlus™ 2020\nUse \"help [command name]\" for more information on it.")

        await ctx.send(embed=embed)
    elif helpmore.lower() == "hello":
        helloembed=discord.Embed(
            title="A small introduction to OnePlus!\nUsage = \".hello\"",
            color=0x00fffb
        )
        await ctx.send(embed=helloembed)
    elif helpmore.lower() == "insult":
        insultembed=discord.Embed(
            title="Insult someone, or just generate one!\n Usage = \".insult @user\" or \".insult\""
        )
        await ctx.send(embed=insultembed)
    elif helpmore.lower() == "randomlenny":
        lennyembed=discord.Embed(
            title="Generate a random lenny face!\nUsage = \".randomlenny\"",
            color=0x00fffb
        )
        await ctx.send(embed=lennyembed)
    elif helpmore.lower() == "btcprice":
        btcpembed=discord.Embed(
            title="The current price of Bitcoin\nUsage = \".btcprice usd\" or \".btcprice gbp\"",
            color=0x00fffb
        )
        await ctx.send(embed=btcpembed)
    elif helpmore.lower() == "genuser":
        genuserembed=discord.Embed(
            title="Create a username! (Using a name to base it off of.)\nUsage = \".genuser basename\"",
            color=0x00fffb
        )
        await ctx.send(embed=genuserembed)
    elif helpmore.lower() == "covid":
        covidembed=discord.Embed(
            title="The current amount of COVID-19 cases/recoveries/deaths\nUsage = \".covid cases/deaths/recovered\"",
            color=0x00fffb
        )
        await ctx.send(embed=covidembed)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

client.run("NzQ2MDk4Mjk4Njk5NjQ0OTU5.Xz7YMA.HwR2mJsZcPHqFSIEEMZmxcfoxMc")