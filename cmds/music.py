import discord
from discord.ext import commands
from core.classes import cog_extension
import json
import random
import youtube_dl

class music(cog_extension):

  players = {}

  @commands.command()
  async def disconnect(self,ctx):
    await ctx.voice_client.disconnect()

  @commands.command()
  async def play(self,ctx,url):
    with open("music.json","r",encoding='utf8') as f:
      music= json.load(f)
    music["music"]["again"] = url
    with open("music.json","w",encoding='utf8') as f:
        music= json.dump(music,f)
    if ctx.author.voice is None:
      await ctx.send(f'進一個語音頻道阿')
    else:
      if ctx.voice_client is None:
        await ctx.author.voice.channel.connect()
      else:
        await ctx.voice_client.move_to(ctx.author.voice.channel)
      FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
      YDL_OPTIONS = {'format':"bestaudio"}
      vc = ctx.voice_client

      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url,download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
        vc.play(source)
  @commands.command()
  async def pause(self,ctx):
    await ctx.voice_client.pause()
  @commands.command()
  async def resume(self,ctx):
    await ctx.voice_client.resume()
  
  @commands.command()
  async def again(self,ctx):
    with open("music.json","r",encoding='utf8') as f:
      music= json.load(f)
    url = music["music"]["again"]
    if ctx.author.voice is None:
      await ctx.send(f'進一個語音頻道阿')
    else:
      if ctx.voice_client is None:
        await ctx.author.voice.channel.connect()
      else:
        await ctx.voice_client.move_to(ctx.author.voice.channel)
      FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
      YDL_OPTIONS = {'format':"bestaudio"}
      vc = ctx.voice_client

      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url,download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
        vc.play(source)
  @commands.command()
  async def lm(self,ctx,type1):
    with open("music.json","r",encoding='utf8') as f:
      music= json.load(f)
    musicc = len(music["music"][type1])
    ra = random.randint(1,musicc)
    
    for i in music["music"][type1]:
      if ra == 1:
        await ctx.send(f'now playing: {i}')
        url = music["music"][type1][i]
        break
      else:
        ra-=1
    with open("music.json","r",encoding='utf8') as f:
      music= json.load(f)
    music["music"]["again"] = url
    with open("music.json","w",encoding='utf8') as f:
        music= json.dump(music,f)
    if ctx.author.voice is None:
      await ctx.send(f'進一個語音頻道阿')
    else:
      if ctx.voice_client is None:
        await ctx.author.voice.channel.connect()
      else:
        await ctx.voice_client.move_to(ctx.author.voice.channel)
      FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
      YDL_OPTIONS = {'format':"bestaudio"}
      vc = ctx.voice_client
      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url,download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
        vc.play(source)
  @commands.command()
  async def newm(self,ctx,type1,title,url):
    with open("music.json","r",encoding='utf8') as f:
      music= json.load(f)
    if type1 not in music["music"]:
      music["music"][type1]={}
    music["music"][type1][title]=url
    with open("music.json","w",encoding='utf8') as f:
        music= json.dump(music,f)
    await ctx.send(f'{title}於{type1}新增完成')
  @commands.command()
  async def allm(self,ctx,type1):
    with open("music.json","r",encoding='utf8') as f:
      music= json.load(f)
    for i in music["music"][type1]:
      await ctx.send(i)
      
      


      
        

def setup(client):
  client.add_cog(music(client))