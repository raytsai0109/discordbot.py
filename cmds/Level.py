import discord
from discord.ext import commands
from core.classes import cog_extension
import json


class level(cog_extension):
  @commands.command()
  async def alevel(self,ctx):
    fn = discord.File('Level/Levelall.jpeg')
    await ctx.send(file=fn)

  @commands.command()
  async def level(self,ctx,num):
    fn = discord.File(f'Level/{num}.jpeg')
    await ctx.send(file=fn)
    
  
def setup(client):
  client.add_cog(level(client))