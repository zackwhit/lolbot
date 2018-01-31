#!/usr/local/bin/python3.6

# This is a discord bot to count how many times people say lol
import discord
from discord.ext import commands
import random
import sys
import asyncio
import json


description = "LoL, bot!"
file_loc = "/home/gector/lolbot/"
token_file="/home/gector/discord_bot_token.txt"
token = ""

commands = [
        "lolcheck",
        "lolremove",
        "lolrestart",
        "loladd", 
        "scoreboard",
        "lolscore",
        "lolboard"]

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
    data = 0;
    if message.content.lower().find("lolcheck") != -1:
        with open(file_loc + "count.txt") as file:
            num = file.readline(9999).strip()
            await bot.send_message(message.channel, "We have a total of {} \'lol\'s so far".format(num))

    if message.content.lower().find("lolrestart") != -1:
        await bot.send_message(message.channel, "AHHHhh!")
        await bot.send_message(message.channel, "Restarting: " + message.author.nick);
        #sys.exit()
        raise SystemExit(0)
    if message.content.lower().find("lolscore") != -1:
        with open('data.json') as json_data:
            data = json.load(json_data)
        await bot.send_message(message.channel, message.author.name + ": " + str(data[message.author.name.lower()]))

    if message.content.lower().find("lolboard") != -1:
        with open('data.json') as json_data:
            data = json.load(json_data)
        for usr in message.server.members:
            if usr.name.lower() in data and data[usr.name.lower()] != 0:
                await bot.send_message(message.channel, usr.name + ": " + str(data[usr.name.lower()]))

    if message.content.lower().find("lolremove") != -1 and message.author.name.lower().find("gector") != -1:
        msg_args = message.content.split(" ");
        arg1 = int(msg_args[1].strip())
        num = 0
        with open(file_loc + "count.txt") as file:
            num = int(file.readline(9999).strip())
        num = num - arg1
        with open(file_loc + "count.txt", "w") as file:
            file.write(str(num))
        await bot.send_message(message.channel, "\'lol\'s now: " + str(num))

    if message.content.lower().find("loladd") != -1 and message.author.nick.lower().find("gector") != -1:
        msg_args = message.content.split(" ");
        arg1 = int(msg_args[1].strip())
        num = 0
        with open(file_loc + "count.txt") as file:
            num = int(file.readline(9999).strip())
        num = num + arg1
        with open(file_loc + "count.txt", "w") as file:
            file.write(str(num))
        await bot.send_message(message.channel, "\'lol\'s now: " + str(num))

    if message.content.lower().find("lol") != -1 and message.author.name != bot.user.name:
        print("Got lol")

        for x in commands:
            if message.content.lower().find(x) != -1:
                return;
        
        # JSON WIP
        with open('data.json') as json_data:
             data = json.load(json_data)
             print(data)

        for usr in message.server.members:
            if usr.name.lower() not in data:
                data[usr.name.lower()] = 0
        
        data[message.author.name.lower()] += 1

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
            
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
            if message.content.lower().find(x) == -1:
                return;


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

bot.run(token)
