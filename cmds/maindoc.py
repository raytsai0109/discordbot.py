import discord
from discord.ext import commands
from core.classes import cog_extension
import json
import datetime
import random
import asyncio


# async def check_account(user):
#   users = get_bank_data()
#   if str(user.id) in users:
#     return False
#   else:
#     users[str(user.id)] ={}
#     users[str(user.id)]["wallet"]=0
#     with open("bankdata.json","w") as f:
#       users= json.dump(users,f)
#   return True

# async def get_bank_data():
#   with open("bankdata.json","r") as f:
#     users= json.load(f)
#     return users

class Main(cog_extension):
  @commands.command(name='ping')
  async def ping(self,ctx):
    await ctx.channel.send(f'{self.client.latency*1000}/ms')

  @commands.command()
  async def hello(self,ctx):
    await ctx.send(f"Hi <@{ctx.author.id}>")

  @commands.command()    
  async def bank(self,ctx):
    with open("bankdata.json","r") as f:
      users= json.load(f)
    if str(ctx.author.id) not in users:
      users[str(ctx.author.id)] ={}
      users[str(ctx.author.id)]["wallet"]=0
      users[str(ctx.author.id)]["weppon"]=0
      users[str(ctx.author.id)]["shield"]=0
      with open("bankdata.json","w") as f:
        users= json.dump(users,f)
    user = ctx.author
    wallet_amt =users[str(user.id)]["wallet"]
    em = discord.Embed(title = f"{ctx.author.name}'s 錢包", color = discord.Color.red())
    em.set_thumbnail(url = user.avatar_url)
    em.add_field(name = "Wallet", value = wallet_amt)
    await ctx.send(embed = em)

  @commands.command()
  async def daily(self,ctx):
    with open("dailycheck.json","r") as e:
      chemem= json.load(e)
    with open("bankdata.json","r") as f:
      users= json.load(f)
    if str(ctx.author.id) not in chemem :
      daicoin = random.randint(150,750)
      await ctx.channel.send(f'<@{ctx.author.id}> 獲得每日獎勵{daicoin}')
      users[str(ctx.author.id)]["wallet"] +=daicoin
      chemem[str(ctx.author.id)] ={}
      with open("dailycheck.json","w") as e:
        chemem= json.dump(chemem,e)
      with open("bankdata.json","w") as f:
        users= json.dump(users,f)
    else:
      await ctx.channel.send(f'已領取本日獎勵')

  @commands.command()
  async def lottery(self,ctx):
    with open("bankdata.json","r") as f:
      users= json.load(f)
    if users[str(ctx.author.id)]["wallet"] >=30:
      lot = random.randint(1,40)
      userlot = random.randint(1,40)
      await ctx.channel.send(f'中獎號碼為{lot}')
      await ctx.channel.send(f'你的號碼為{userlot}')
      if lot == userlot:
        prizenum = random.randint(1500,2500)
        await ctx.channel.send(f'<@{ctx.author.id}>恭喜中獎獲得{prizenum}元！')
        users[str(ctx.author.id)]["wallet"] +=(prizenum-30)
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
      else:
        await ctx.channel.send(f'很抱歉,你沒有中獎')
        users[str(ctx.author.id)]["wallet"] -=30
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
    else:
      await ctx.channel.send(f'餘額不足,窮逼')


  @commands.command()
  async def scoticket(self,ctx,amount):
    with open("bankdata.json","r") as f:
      users= json.load(f)
    amount = int(amount)
    if str(ctx.author.id) in users and users[str(ctx.author.id)]["wallet"] >= amount:
      scran = random.randint(1,1000)
      if scran <=500:
        await ctx.channel.send(f'很抱歉，啥都沒刮到')
        am = amount
        users[str(ctx.author.id)]["wallet"] -=am
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
      elif scran >500 and scran <=650:
        await ctx.channel.send(f'<@{ctx.author.id}>恭喜刮中{amount/2}元')
        mon = amount/2
        users[str(ctx.author.id)]["wallet"] -=mon
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
      elif scran >650 and scran <= 800:
        await ctx.channel.send(f'<@{ctx.author.id}>恭喜刮中{amount}元')
      elif scran >800 and scran <=950:
        await ctx.channel.send(f'<@{ctx.author.id}>恭喜刮中{amount*1.5}元')
        mon = amount/2
        users[str(ctx.author.id)]["wallet"] +=mon
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
      elif scran >950 and scran <=990:
        await ctx.channel.send(f'<@{ctx.author.id}>恭喜刮中{amount*4}元')
        mon = amount*3
        users[str(ctx.author.id)]["wallet"] +=mon
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
      elif amount >=1000 and scran <=997:
        await ctx.channel.send(f'<@{ctx.author.id}>恭喜刮中二獎$50000元')
        won = 50000-amount
        users[str(ctx.author.id)]["wallet"] +=won
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
      elif amount >=1000 and scran <=1000:
        await ctx.channel.send(f'<@{ctx.author.id}>恭喜刮中頭獎$100000元')
        won = 100000-amount
        users[str(ctx.author.id)]["wallet"] +=won
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
      else:
        await ctx.channel.send(f'<@{ctx.author.id}>恭喜刮中{amount*4}元')
        mon = amount*3
        users[str(ctx.author.id)]["wallet"] +=mon
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
    else:
      await ctx.channel.send(f'自以為幽默 低能兒')

  @commands.command()
  async def buywep(self,ctx,num):
    with open("bankdata.json","r") as f:
      users= json.load(f)
    num=int(num)
    if users[str(ctx.author.id)]["wallet"] >=1000*num:
      wepnum =0
      for a in range(0,num):
        b=random.randint(1,4)
        if b==3:
          wepnum+=1
      if wepnum !=0:
        users[str(ctx.author.id)]["wallet"]-=1000*num
        users[str(ctx.author.id)]["weppon"]+=wepnum
        with open("bankdata.json","w") as f:
            users= json.dump(users,f)
        await ctx.channel.send(f'你成功購買了{wepnum}個錘子')
      else:
        await ctx.channel.send(f'購買交易失敗')
        users[str(ctx.author.id)]["wallet"]-=1000*num
        with open("bankdata.json","w") as f:
            users= json.dump(users,f)
    else:
      await ctx.channel.send(f'?????')
  
  @commands.command()
  async def wep(self,ctx):
    with open("bankdata.json","r") as f:
      users= json.load(f)
    user = ctx.author
    wep_amt =users[str(user.id)]["weppon"]
    em = discord.Embed(title = f"{ctx.author.name}'s 錘子", color = discord.Color.red())
    em.set_thumbnail(url = user.avatar_url)
    em.add_field(name = "Weapon", value = wep_amt)
    await ctx.send(embed = em)

  @commands.command()
  async def attack(self,ctx,member:discord.Member):
    with open("bankdata.json","r") as f:
      users= json.load(f)
    if users[str(ctx.author.id)]["weppon"] >0 and users[str(member.id)]["shield"]==0:
      randnum = random.randint(1,5)
      minus = users[str(member.id)]["wallet"]*randnum/100
      users[str(member.id)]["wallet"] -=minus
      users[str(ctx.author.id)]["wallet"]+=minus
      users[str(ctx.author.id)]["weppon"]-=1
      with open("bankdata.json","w") as f:
        users= json.dump(users,f)
      await ctx.channel.send(f'<@{ctx.author.id}>你幹走<@{member.id}> {minus}元')
    elif users[str(ctx.author.id)]["weppon"]<=0:
      await ctx.channel.send(f'是在哭嗎?')
    else:
      if users[str(member.id)]["shield"]>0:
        users[str(member.id)]["shield"]-=1
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
      await ctx.channel.send(f'<@{member.id}>護盾-1')

  @commands.command()
  async def send(self,ctx,member:discord.Member,amount):
    with open("bankdata.json","r") as f:
      users= json.load(f)
    if str(ctx.author.id) in users and str(member.id) in users:
      amount = int(amount)
      if amount > users[str(ctx.author.id)]["wallet"] or amount <=0 :
        await ctx.channel.send(f'自以為幽默 低能兒')
      else:
        users[str(ctx.author.id)]["wallet"] -=amount
        users[str(member.id)]["wallet"] +=amount
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
        await ctx.channel.send(f'<@{ctx.author.id}>你給了<@{member.id}> {amount}塊錢')
  
  @commands.command()
  async def givewep(self,ctx,member:discord.Member,amount):
    with open("bankdata.json","r") as f:
      users= json.load(f)
    if str(ctx.author.id) in users and str(member.id) in users:
      amount = int(amount)
      if amount > users[str(ctx.author.id)]["weppon"] or amount <=0 :
        await ctx.channel.send(f'自以為幽默 低能兒')
      else:
        users[str(ctx.author.id)]["weppon"] -=amount
        users[str(member.id)]["weppon"] +=amount
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
        await ctx.channel.send(f'<@{ctx.author.id}>你給了<@{member.id}> {amount}個錘子')

  @commands.command()
  async def mine(self,ctx):
    with open("bankdata.json","r") as f:
      users= json.load(f)
    if users[str(ctx.author.id)]["wallet"] >=10:
      await ctx.channel.send(f'挖礦中...')
      rantime = random.randint(2,5)
      await asyncio.sleep(rantime)
      users[str(ctx.author.id)]["wallet"]-=10
      with open("bankdata.json","w") as f:
        users= json.dump(users,f)
      with open("bankdata.json","r") as f:
        users= json.load(f)
      minenum = random.randint(1,1000)
      if minenum >315:
        await ctx.channel.send(f'沒挖到任何東西')
      elif minenum >30:
        minerand = random.randint(50,300)
        users[str(ctx.author.id)]["wallet"]+=minerand
        with open("bankdata.json","w") as f:
            users= json.dump(users,f)
        await ctx.channel.send(f'<@{ctx.author.id}>你挖到了{minerand}元')
      elif minenum >20:
        users[str(ctx.author.id)]["weppon"]+=1
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
        await ctx.channel.send(f'<@{ctx.author.id}>你挖到了1個錘子')
      elif minenum >10:
        users[str(ctx.author.id)]["shield"]+=1
        with open("bankdata.json","w") as f:
          users= json.dump(users,f)
        await ctx.channel.send(f'<@{ctx.author.id}>你挖到了1個護盾')
      else:
        with open("coindata.json","r") as a:
          cusers = json.load(a)
        if str(ctx.author.id) in cusers:
          cusers[str(ctx.author.id)]["wallet"]+=1
          with open("coindata.json","w") as a:
            cusers= json.dump(cusers,a)
          await ctx.channel.send(f'<@{ctx.author.id}>你挖到了1塊幣')
    else:
      await ctx.channel.send(f'餘額不足,窮逼')

  @commands.command()
  async def buyshield(self,ctx,num):
    num = int(num)
    if num >10:
      num=10
    with open("bankdata.json","r") as f:
      users= json.load(f)
    if users[str(ctx.author.id)]["wallet"]>num*1000:
      users[str(ctx.author.id)]["shield"]+=num;
      users[str(ctx.author.id)]["wallet"]-=num*1000
      with open("bankdata.json","w") as f:
        users= json.dump(users,f)
      await ctx.channel.send(f'你購買了{num}個護盾')
    else:
      await ctx.channel.send(f'餘額不足,窮逼')

  @commands.command()
  async def shield(self,ctx):
    with open("bankdata.json","r") as f:
      users= json.load(f)
    user = ctx.author
    shield_amt =users[str(user.id)]["shield"]
    em = discord.Embed(title = f"{ctx.author.name}'s 護盾", color = discord.Color.red())
    em.set_thumbnail(url = user.avatar_url)
    em.add_field(name = "shield", value = shield_amt)
    await ctx.send(embed = em)

  @commands.command()
  async def waifu(self,ctx):
    with open("waifu.json","r",encoding='utf8') as f:
      pictures= json.load(f)
    wl = len(pictures)
    wc = random.randint(1,wl)
    for b in pictures:
      if  wc==1:
        with open("waifucost.json","r",encoding='utf8') as c:
          picturecost= json.load(c)
        pic = pictures[b]
        picost = picturecost[b+"cost"]
        embed=discord.Embed(title="Cost", description=f'${picost}')
        embed.set_author(name=b)
        embed.set_image(url=pic)
        await ctx.send(embed=embed)
        wc-=1
        def check(number):
          return number.author == ctx.author and number.channel == ctx.message.channel
        response = await self.client.wait_for('message',check=check)
        try:
          asw = response.content
        except:
          pass
        if asw =='buy':
          with open("coindata.json","r") as f:
            users = json.load(f)
          picost = int(picost)
          if users[str(ctx.author.id)]["wallet"]>=picost:
            users[str(ctx.author.id)]["wallet"]-=picost
            with open("coindata.json","w") as f:
              users = json.dump(users,f)
            await ctx.channel.send(f'<@{ctx.author.id}>你購買了{b}')
          else:
            await ctx.channel.send(f'貓貓幣餘額不足')
      else:
        wc-=1 
    else:
      pass 
  @commands.command()
  async def allwaifu(self,ctx):
    with open("waifu.json","r",encoding='utf8') as f:
      pictures= json.load(f)
    for i in pictures:
      await ctx.channel.send(i)

  @commands.command()
  async def dclear(self,ctx):
    with open("dailycheck.json","r") as f:
      users= json.load(f)
    users = {}
    with open("dailycheck.json","w") as f:
      users = json.dump(users,f)
    await ctx.send(f'每日更新完成')

  @commands.command()
  async def catcoin(self,ctx):
    with open("coindata.json","r") as f:
      users= json.load(f)
    if str(ctx.author.id) not in users:
      users[str(ctx.author.id)]={}
      users[str(ctx.author.id)]["wallet"]=0
      with open("coindata.json","w") as f:
        users = json.dump(users,f)
      await ctx.send(f'join success')
    else:
      await ctx.send(f'你有{users[str(ctx.author.id)]["wallet"]}顆貓貓幣')

  @commands.command()
  async def pwaifu(self,ctx,msg,url):
    with open("waifu.json","r",encoding='utf8') as f:
      users= json.load(f)
    with open("waifucost.json","r",encoding='utf8') as c:
      userscost= json.load(c)
    users[msg] = url 
    with open("waifu.json","w",encoding='utf8') as f:
      users = json.dump(users,f)
    userscost[msg+"cost"] = "1"
    with open("waifucost.json","w",encoding='utf8') as f:
      userscost = json.dump(userscost,f)
    

  @commands.command()
  async def ccc(self,ctx):
    with open("coindata.json","r") as f:
      users = json.load(f)
    count =0
    for a in users:
      if users[a]["wallet"] !=0:
        count += int(users[a]["wallet"])
    await ctx.send(count)
    
    
    

def setup(client):
  client.add_cog(Main(client))