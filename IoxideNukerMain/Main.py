class ServerNuker():
    _version_ = 1

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

ctypes.windll.kernel132.SetConsoleTileW(f'[Ioxide Server Nuker v{ServerNuker._version_}] | Loading in...')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('pass')
prefix = config.get('prefix')
anti_afk = config.get('anti_afk')

width = os.get_terminal_size().columns
 def RandomColor():
     if anti_afk == True:
         anti_afk = 'Active'
    else:
        anti_afk = 'Off'

     print(f'''{Fore.RESET}
                    {Fore.Green} ██▓ ▒█████  ▒██   ██▒ ██▓▓█████▄ ▓█████ 
                    {Fore.Green}▓██▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▒██▀ ██▌▓█   ▀ 
                    {Fore.Green}▒██▒▒██░  ██▒░░  █   ░▒██▒░██   █▌▒███   
                    {Fore.Green}░██░▒██   ██░ ░ █ █ ▒ ░██░░▓█▄   ▌▒▓█  ▄ 
                    {Fore.Green}░██░░ ████▓▒░▒██▒ ▒██▒░██░░▒████▓ ░▒████▒
                    {Fore.Green}░▓  ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓   ▒▒▓  ▒ ░░ ▒░ ░
                    {Fore.Green} ▒ ░  ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░
                    {Fore.Green} ▒ ░░ ░ ░ ▒   ░    ░   ▒ ░ ░ ░  ░    ░   
                    {Fore.Green} ░      ░ ░   ░    ░   ░     ░       ░  ░
                    {Fore.Green}                           ░             
                                    
                        {Fore.Green}Logged In As ==> {Fore.WHITE}{Ioxide.user.name}#{Ioxide.user.discriminator}{Fore.WHITE}
                        {Fore.Green}ID ==> {Fore.WHITE}{Ioxide.user.id}
                        {Fore.Green}Packer ==> {Fore.WHITE}{packer}
                        {Fore.Green}Anti-AFK ==> {Fore.WHITE}{antiafk}
                        {Fore.Green}Version ==> {Fore.RED} v{ServerNuker._version_}
                    '''+Fore.RESET
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
            os.system(f'title [ Ioxide Packing Tool ] - Version {ChatPacker.__version__}')
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
    description='Ioxide Packing Tool',
    command_prefix=prefix,
    self_bot=True
)
