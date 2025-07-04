import discord
import os
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def randommem(ctx):
    files = os.listdir("images")#images dosyasını list olarak tanımlıyo
    img_name = random.choice(files)#images dosyasındaki resimleri rasgele seçer
    with open(f"images/{img_name}","rb")as f: #
        picture = discord.File(f) #resimleri discordun anlayabileceği dosyaya çevirir
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    image_urls = get_dog_image_url()
    await ctx.send(image_urls)

@bot.command()
async def çevre_kirliliği_hakkında_birşeyler(ctx):
    await ctx.send("senin için şunalrı buldum:https://www.ankara.bel.tr/files/7414/3695/0096/1-cevrebilgisi-16_SAYFA.pdf    !!!Daha Fazlası için:$dahafazlasoru yazınız")

@bot.command()
async def dahafazlasoru(ctx):
    await ctx.send("daha fazla sorular için:https://camlicacevre.com/cevre-kirliligi-nedir-neden-olur-nasil-onlenir/   !!!atık kaybolma süreleri için:$atıkkaybolma yazınız")


@bot.command()
async def atıkkaybolma(ctx):
    with open('çevrefoto/image1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)





bot.run("")
