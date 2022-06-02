import discord
from discord.ext import commands
from core.classes import cog_extension
import json
import random


class pokers(cog_extension):
  @commands.command()
  async def lineup(self,ctx):
    with open("lineup.json","r",encoding='utf8') as f:
      users= json.load(f)
    a=0
    for i in users:
      if users[i]["lineup"] > a:
        a=users[i]["lineup"]
    if str(ctx.author.id)not in users:
      users[str(ctx.author.id)]={}
      users[str(ctx.author.id)]["lineup"]=a+1
      with open("lineup.json","w") as f:
        users= json.dump(users,f)
      await ctx.send(f'加入成功 你還需要等{a}號')
    if users[str(ctx.author.id)]["lineup"]==0:
      with open("lineup.json","r",encoding='utf8') as f:
        users= json.load(f)
      users[str(ctx.author.id)]["lineup"]=a+1
      with open("lineup.json","w") as f:
        users= json.dump(users,f)
      await ctx.send(f'加入成功 你還需要等{a}號')
    else:
      await ctx.send(f'你已加入排隊序列中')
    
          
  @commands.command()
  async def football(self,ctx,amount):
    with open("lineup.json","r",encoding='utf8') as f:
      users= json.load(f)
    with open("bankdata.json","r",encoding='utf8') as f:
      coin= json.load(f)
    amount = int(amount)
    if amount <= coin[str(ctx.author.id)]["wallet"] and amount%1000==0 and amount>=1000: 
      if users[str(ctx.author.id)]["lineup"]==1:
        a=random.randint(1,52)
        b=random.randint(1,52)
        c=random.randint(1,52)
        while a==b or b==c or a==c:
          b=random.randint(1,52)
          c=random.randint(1,52)
        if a<=13:
          atype = 'c'
        elif a<=26:
          atype = 'd'
        elif a<=39:
          atype = 'h'
        else:
          atype = 's'
        if b<=13:
          btype = 'c'
        elif b<=26:
          btype = 'd'
        elif b<=39:
          btype = 'h'
        else:
          btype = 's'
        if c<=13:
          ctype = 'c'
        elif c<=26:
          ctype = 'd'
        elif c<=39:
          ctype = 'h'
        else:
          ctype = 's'
        a=a%13
        b=b%13
        c=c%13
        a=str(a)
        b=str(b)
        c=str(c)
        if a=='0':
          a='13'
        if b=='0':
          b='13'
        if c=='0':
          c='13'
        await ctx.send(f'球柱為:')
        ad = discord.File(f'pokers52/{atype}{a}.jpg')
        await ctx.send(file=ad)
        bd = discord.File(f'pokers52/{btype}{b}.jpg')
        await ctx.send(file=bd)
        if a==b:
          await ctx.send(f'請輸入up或down來猜測你的牌對於球柱的大小')
        def check(number):
          return number.author == ctx.author and number.channel == ctx.message.channel
        response = await self.client.wait_for('message',check=check)
        try:
          asw = response.content
        except:
            pass
        if asw =='open':
          cd = discord.File(f'pokers52/{ctype}{c}.jpg')
          await ctx.send(file=cd)
          a=int(a)
          b=int(b)
          c=int(c)
          if a>c>b or b>c>a:
            coin[str(ctx.author.id)]["wallet"]+=amount*1
            with open("bankdata.json","w") as f:
              coin= json.dump(coin,f)
            await ctx.send(f'<@{ctx.author.id}>成功射進球門，贏了{amount*2}元')
          elif a==c or b==c:
            coin[str(ctx.author.id)]["wallet"]-=amount*2
            with open("bankdata.json","w") as f:
              coin= json.dump(coin,f)
            await ctx.send(f'<@{ctx.author.id}>撞柱，賠了{amount*2}元')
          else:
            coin[str(ctx.author.id)]["wallet"]-=amount
            with open("bankdata.json","w") as f:
              coin= json.dump(coin,f)
            await ctx.send(f'<@{ctx.author.id}>未射進球門，賠了{amount}元')
          if asw =='up'and int(a)==int(b):
            cd = discord.File(f'pokers52/{ctype}{c}.jpg')
            await ctx.send(file=cd)
            a=int(a)
            b=int(b)
            c=int(c)
            if c>a:
              coin[str(ctx.author.id)]["wallet"]+=amount*1
              with open("bankdata.json","w") as f:
                coin= json.dump(coin,f)
              await ctx.send(f'<@{ctx.author.id}>恭喜猜對 贏了{amount}元')
            elif c==a:
              await ctx.send(f'再次撞柱 本局不算')
            else:
              coin[str(ctx.author.id)]["wallet"]-=amount*1
              with open("bankdata.json","w") as f:
                coin= json.dump(coin,f)
              await ctx.send(f'<@{ctx.author.id}>猜錯 賠了{amount}元')
          if asw =='down' and int(a)==int(b):
            cd = discord.File(f'pokers52/{ctype}{c}.jpg')
            await ctx.send(file=cd)
            a=int(a)
            b=int(b)
            c=int(c)
            if c<a:
              coin[str(ctx.author.id)]["wallet"]+=amount*1
              with open("bankdata.json","w") as f:
                coin= json.dump(coin,f)
              await ctx.send(f'<@{ctx.author.id}>恭喜猜對 贏了{amount}元')
            elif c==a:
              await ctx.send(f'再次撞柱 本局不算')
            else:
              coin[str(ctx.author.id)]["wallet"]-=amount*1
              with open("bankdata.json","w") as f:
                coin= json.dump(coin,f)
              await ctx.send(f'<@{ctx.author.id}>猜錯 賠了{amount}元')
      else:
        await ctx.send('還未輪到你')
    else:
      await ctx.send(f'未符合籌碼標準或餘額不足')
    for m in users:
      if users[m]["lineup"]!=0:
        users[m]["lineup"]-=1
        with open("lineup.json","w") as f:
          users= json.dump(users,f)
        if users[m]["lineup"]==1:
          await ctx.send(f'<@{m}>下一個輪到你了')
    
  @commands.command()
  async def mynum(self,ctx):
    with open("lineup.json","r",encoding='utf8') as f:
      users= json.load(f)
    if str(ctx.author.id) in users:
      if users[str(ctx.author.id)]["lineup"]!=0:
        await ctx.send(f'尚餘{users[str(ctx.author.id)]["lineup"]-1}位就輪到你了')
      else:
        await ctx.send(f'你尚未加入排隊號碼中')
    else:
      await ctx.send(f'你尚未加入排隊號碼中')
def setup(client):
  client.add_cog(pokers(client))