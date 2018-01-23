#!/usr/local/bin/python3.6

# This is a discord bot to count how many times people say lol
import discord
from discord.ext import commands
import random
import sys
import asyncio

description = "LoL, bot!"
file_loc = "/home/gector/lolbot"
token_file="/home/gector/discord_bot_token.txt"
token = ""
with open(token_file, 'r') as file:
    token = file.readline(100).strip()
print("Bot token: " + token)

bot = discord.Client() # commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print("Connected!")
    print("Username: " + bot.user.name)
    print('------------------')

@bot.event
async def on_message(message):
    if message.content.lower().find("lol") != -1 and message.author.name != bot.user.name and message.content.lower().find("lolcheck") == -1:
        print("Got lol")
        if random.randint(1, 30) == 15:
            with open(file_loc + "count.txt") as file:
                num = file.readline(99999).strip()
                await bot.send_message(message.channel, "LOL!(x{})".format(num))
        print(message.channel)
        data = {0, 1}
        with open(file_loc + "count.txt") as file:
            data = file.readline(99999).strip()
        with open(file_loc + "count.txt", "w") as file:
            print(data)
            data = int(data) + 1
            file.write(str(data))
    if message.content.lower().find("lolcheck") != -1:
        with open(file_loc + "count.txt") as file:
            num = file.readline(9999).strip()
            await bot.send_message(message.channel, "We have a total of {} \'lol\'s so far".format(num))
    if message.content.lower().find("diediedie") != -1:
        await bot.send_message(message.channel, "AHHHhh!")
        sys.exit()

bot.run(token)
