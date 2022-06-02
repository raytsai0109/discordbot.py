import discord
from discord.ext import commands
from core.classes import cog_extension
import random

class event(cog_extension):
  
  @commands.Cog.listener()
  async def on_message(self,msg):
    if "是不是" in msg.content:
      che = random.randint(0,1)
      if che == 0:
        await msg.channel.send(f'是')
      else:
        await msg.channel.send(f'不是')
    if "有沒有" in msg.content:
      che = random.randint(0,1)
      if che == 0:
        await msg.channel.send(f'有')
      else:
        await msg.channel.send(f'沒有')
      if "會不會" in msg.content:
        che = random.randint(0,1)
        if che == 0:
          await msg.channel.send(f'會')
        else:
          await msg.channel.send(f'不會')
    if "機率" in msg.content:
      await msg.channel.send(f"{random.randint(1,100)}%")
  
  @commands.Cog.listener()
  async def on_command_error(self,ctx,error):
    if isinstance(error,commands.errors.CommandInvokeError):
       pass
    else:
      await ctx.send(error)
    # if isinstance(error,commands.errors.MissingRequiredArgument):
    #   await ctx.channel.send(f'數值呢?')
    # elif isinstance(error,commands.errors.CommandInvokeError):
    #   await ctx.channel.send(f'數值錯誤')
    # elif isinstance(error,commands.errors.CommandNotFound):
    #   await ctx.channel.send(f'????')
    # else:
    #   await ctx.channel.send(error)
    
    

def setup(client):
  client.add_cog(event(client))
