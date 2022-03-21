import discord
from discord.ext import commands
from discord.utils import get
import pandas as pd

intents = discord.Intents.default()
intents.members = True 
bot = commands.Bot(intents=intents, command_prefix="!")

# Event to make sure the bot is live
@bot.event
async def on_ready():
    print("Bot is live")

users = []

# To get users by roles => !users_list roles_wanted (ex: !users_list Dev)
@bot.command(name="users_list")
async def usersList(ctx, role_wanted):
    users.clear()
    members = ctx.guild.members
    for member in members:
        try:
            print(member.roles)
            for role in member.roles:
                if role.name == role_wanted:
                    print(member.name + ' is ' + role.name)
                    users.append(member.name)
                else: 
                    print(member.name + ' is not a ' + role.name)
        except:
            print("no members")
    df = pd.DataFrame(users, columns= ["Users with role '" + role_wanted + "'"])
    df.to_csv ('export_dataframe.csv', index = False, header=True)
    print (df)

bot.run("OTU1NTIzNDA3MDQ1MzUzNTQz.Yji6hQ.5vICSyxRcDS-LuxRAOfbm47Dh1w")