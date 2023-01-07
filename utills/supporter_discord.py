import discord
from discord.ext import commands
import datetime
import os
import sqlite3
import pickle

def init():
    global token
    global db_addr # Database address
    global cache_addr # Cache address
    global cache

    token = 'MTA2MDQ0NzQzNDQ3NzY4Mjc1OA.GOmFza.P15N4moodQvPgJ3sBvp7LowKNx_suCHEPBANaI'
    db_addr = './utills/database.db'
    cache_addr = './utills/memory.cache'

    if not os.path.isfile(db_addr):
        con = sqlite3.connect(db_addr) # Make a database
        cur = con.cursor() # Connect
        cur.execute("CREATE TABLE PLAN(year text, month text, day text, hour text, minute text, content text);") # Create table for making plans
        con.commit() # Save a database
        cur.close()
        con.close()

    

init() # Initalize

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def make_plan(ctx, msg):
    if not msg == 'help':
        msg = msg.split(':')
        date = msg[0].rstrip().split('/')
        content = [msg[1].lstrip()]
        con = sqlite3.connect(db_addr)
        cur = con.cursor()

        if len(date) == 5:
            plan = date + content
            cur.execute('INSERT INTO PLAN VALUES(?, ?, ?, ?, ?, ?);', (plan))
            con.commit()
            cur.close()
            con.close()
            await ctx.send('ok!')

        elif len(date) == 3:
            now = datetime.datetime.now()
            plan = [now.year, now.month] + date + content
            cur.execute('INSERT INTO PLAN VALUES(?, ?, ?, ?, ?, ?);', (plan))
            con.commit()
            cur.close()
            con.close()
            await ctx.send('ok!')
        else:
            await ctx.send('You can see the help : /make_plan')
    else:
        await ctx.send('Please keep this format "year/month/day/hour/minute/ : content"')
        await ctx.send('Or "day/hour/minute : content"')

bot.run(token)