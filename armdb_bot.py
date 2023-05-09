#/usr/bin/python3

from __future__ import unicode_literals
import time
import discord
import armdb_token
from discord.ext import commands
import os
from pathlib import Path
from actors import get_filmography
import top

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix = "$", intents=intents)
    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    
@bot.command()
async def ping(ctx):
    """A simple test, bot responds 'pong' """
    await ctx.channel.send("pong")
    
@bot.command()
async def actor(ctx, content='actor'):
    """Gives filmography for an actor.  $actor <actor name in quotes>"""
    filmography = get_filmography(content)
    await ctx.send('Filmography of ' + content)
    for i in filmography:
        await ctx.send(i)
        
        
#@bot.command()
#async def top_actors(ctx, number: int):
    """Gives the x most frequent actors on the spreadsheet. $top_actors <number>"""
    #count_list = top.create_count_list()
    #for i in range(number):
        #await ctx.send(count_list[i][0] + " is in " + str(count_list[i][1]) + " movies from the spreadsheet.")"""
        
@bot.command()
async def top_actors(ctx, number: int):
    """Gives the x most frequent actors on the spreadsheet. $top_actors <number>"""
    count_list = top.create_count_list(number)
    for i in range(number):
        await ctx.send(count_list[i][0] + " is in " + str(count_list[i][1]) + " movies from the spreadsheet.")
        
@bot.command()
async def in_movie(ctx, content='actor'):
    """Gives all movies from the spreadshet that the given actor was in. $in_movie <actor name in quotes>"""
    await ctx.send("Movies from the spreadsheet with " + content)
    for movie in top.in_movie_check(content):
        await ctx.send(movie)
        
@bot.command()
async def in_common(ctx, content1='actor1',content2='actor2'):
    """Gives all movies from the spreadshet that the given actors were in together. $in_common <actor_name1 actor_name2> in quotes>"""
    await ctx.send("Movies from the spreadsheet with " + content1 + " & " + content2)
    for movie in top.actor_compare(content1,content2):
        await ctx.send(movie)
@bot.command()

async def castlist(ctx, content='movie_title'):
    """Gives the cast list for a given movie.  $castlist <movie title> 2 in quotes>"""
    await ctx.send("The cast list for " + content)
    for actor in top.get_castlist(content):
        await ctx.send(actor)   
        
bot.run(armdb_token.token)
