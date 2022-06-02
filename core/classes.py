import discord
from discord.ext import commands
import youtube_dl

class cog_extension(commands.Cog):
  def __init__(self,client):
    self.client = client