from ast import alias
from turtle import color, title
from unicodedata import name
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import requests,json
from config import token


client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)

##################### /STAT NA
@slash.slash(name="istatistik-na", description="na (Kuzey Amerika) sunucusundaki oyuncuların istatisliklerini sorguluyabilirsiniz",)
async def slashna(ctx:SlashContext, oyuncu_adı):
    await ctx.defer("Bot Düşünüyor")
    response = requests.get("https://vlrggapi.herokuapp.com/stats/na")
    json_data = json.loads(response.text)
    oyuncular = []
    for dict in json_data["data"]["segments"]:
        for dict in json_data["data"]["segments"]:
            oyuncular.append(dict)
            isim = oyuncu_adı
        for oyuncu in oyuncular:
         if oyuncu["player"] == isim:
            embed = discord.Embed(
        title = "Oyuncu Adı: " + oyuncu["player"],
        description = "・ Oyuncu Takımı: " + oyuncu["org"] + "\n ・  Oyuncu KDA: " + oyuncu["kill_deaths"] + "\n ・  Ortlama Raund Hasarı: " + oyuncu["average_damage_per_round"] + 
        "\n ・  Ortlama Raund Asisti: "+ oyuncu["assists_per_round"] + "\n ・ Headshot Yüzdesi : " + oyuncu["headshot_percentage"] + "\n ・ Clutch Başarı Yüzdesi : " + oyuncu["clutch_success_percentage"] +
        "\n ・ İlk Kan Oranı: " + oyuncu["first_kills_per_round"] + "\n ・ İlk Ölme Oranı : " + oyuncu["first_deaths_per_round"],
        color = discord.Color.random()
    )
            embed.add_field(name='Oyuncu Profili' ,value=f'[Oyuncu Profili İçin Tıkla](https://www.vlr.gg/search/?q={isim})', inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/954724771034198036/957238194917736459/image.gif"),
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/748960804610768947/957300083756527656/logo.png")
            await ctx.send(embed=embed)
            break
        break


########### STAT NA
class statsystemna:
    @client.command(aliases=["istatistik-na"])
    async def statna(ctx, oyuncu_adı):
        response = requests.get("https://vlrggapi.herokuapp.com/stats/na")
        json_data = json.loads(response.text)
        oyuncular = []
        for dict in json_data["data"]["segments"]:
            for dict in json_data["data"]["segments"]:
                oyuncular.append(dict)
            isim = oyuncu_adı
        for oyuncu in oyuncular:
         if oyuncu["player"] == isim:
            embed = discord.Embed(
        title = "Oyuncu Adı: " + oyuncu["player"],
        description = "・ Oyuncu Takımı: " + oyuncu["org"] + "\n ・  Oyuncu KDA: " + oyuncu["kill_deaths"] + "\n ・  Ortlama Raund Hasarı: " + oyuncu["average_damage_per_round"] + 
        "\n ・  Ortlama Raund Asisti: "+ oyuncu["assists_per_round"] + "\n ・ Headshot Yüzdesi : " + oyuncu["headshot_percentage"] + "\n ・ Clutch Başarı Yüzdesi : " + oyuncu["clutch_success_percentage"] +
        "\n ・ İlk Kan Oranı: " + oyuncu["first_kills_per_round"] + "\n ・ İlk Ölme Oranı : " + oyuncu["first_deaths_per_round"],
        color = discord.Color.random()
    ) 
            embed.add_field(name='Oyuncu Profili' ,value=f'[Oyuncu Profili İçin Tıkla](https://www.vlr.gg/search/?q={isim})', inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/954724771034198036/957238194917736459/image.gif"),
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/748960804610768947/957300083756527656/logo.png")
            await ctx.send(embed=embed)
            break
    
###########


##################### /STAT EU
@slash.slash(name="istatistik-eu", description="eu (Avrupa) sunucusundaki oyuncuların istatisliklerini sorguluyabilirsiniz",)
async def slasheu(ctx:SlashContext, oyuncu_adı):
    await ctx.defer("Bot Düşünüyor")
    response = requests.get("https://vlrggapi.herokuapp.com/stats/eu")
    json_data = json.loads(response.text)
    oyuncular = []
    for dict in json_data["data"]["segments"]:
        for dict in json_data["data"]["segments"]:
            oyuncular.append(dict)
            isim = oyuncu_adı
        for oyuncu in oyuncular:
         if oyuncu["player"] == isim:
            embed = discord.Embed(
        title = "Oyuncu Adı: " + oyuncu["player"],
        description = "・ Oyuncu Takımı: " + oyuncu["org"] + "\n ・  Oyuncu KDA: " + oyuncu["kill_deaths"] + "\n ・  Ortlama Raund Hasarı: " + oyuncu["average_damage_per_round"] + 
        "\n ・  Ortlama Raund Asisti: "+ oyuncu["assists_per_round"] + "\n ・ Headshot Yüzdesi : " + oyuncu["headshot_percentage"] + "\n ・ Clutch Başarı Yüzdesi : " + oyuncu["clutch_success_percentage"] +
        "\n ・ İlk Kan Oranı: " + oyuncu["first_kills_per_round"] + "\n ・ İlk Ölme Oranı : " + oyuncu["first_deaths_per_round"],
        color = discord.Color.random()
    ) 
            embed.add_field(name='Oyuncu Profili' ,value=f'[Oyuncu Profili İçin Tıkla](https://www.vlr.gg/search/?q={isim})', inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/954724771034198036/957238194917736459/image.gif"),
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/748960804610768947/957300083756527656/logo.png")
            await ctx.send(embed=embed)
            break
        break


########### STAT EU
class statsystemeu:
    @client.command(aliases=["istatistik-eu"])
    async def stateu(ctx, oyuncu_adı):
        response = requests.get("https://vlrggapi.herokuapp.com/stats/eu")
        json_data = json.loads(response.text)
        oyuncular = []
        for dict in json_data["data"]["segments"]:
            for dict in json_data["data"]["segments"]:
                oyuncular.append(dict)
            isim = oyuncu_adı
        for oyuncu in oyuncular:
         if oyuncu["player"] == isim:
            embed = discord.Embed(
        title = "Oyuncu Adı: " + oyuncu["player"],
        description = "・ Oyuncu Takımı: " + oyuncu["org"] + "\n ・  Oyuncu KDA: " + oyuncu["kill_deaths"] + "\n ・  Ortlama Raund Hasarı: " + oyuncu["average_damage_per_round"] + 
        "\n ・  Ortlama Raund Asisti: "+ oyuncu["assists_per_round"] + "\n ・ Headshot Yüzdesi : " + oyuncu["headshot_percentage"] + "\n ・ Clutch Başarı Yüzdesi : " + oyuncu["clutch_success_percentage"] +
        "\n ・ İlk Kan Oranı: " + oyuncu["first_kills_per_round"] + "\n ・ İlk Ölme Oranı : " + oyuncu["first_deaths_per_round"],
        color = discord.Color.random()
    ) 
            embed.add_field(name='Oyuncu Profili' ,value=f'[Oyuncu Profili İçin Tıkla](https://www.vlr.gg/search/?q={isim})', inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/954724771034198036/957238194917736459/image.gif"),
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/748960804610768947/957300083756527656/logo.png")
            await ctx.send(embed=embed)
            break
###########

########### /STAT AP
@slash.slash(name="istatistik-ap", description="ap (Pasifik Asya) sunucusundaki oyuncuların istatisliklerini sorguluyabilirsiniz",)
async def slashpa(ctx:SlashContext, oyuncu_adı):
    await ctx.defer("Bot Düşünüyor")
    response = requests.get("https://vlrggapi.herokuapp.com/stats/ap")
    json_data = json.loads(response.text)
    oyuncular = []
    for dict in json_data["data"]["segments"]:
        for dict in json_data["data"]["segments"]:
            oyuncular.append(dict)
            isim = oyuncu_adı
        for oyuncu in oyuncular:
         if oyuncu["player"] == isim:
            embed = discord.Embed(
        title = "Oyuncu Adı: " + oyuncu["player"],
        description = "・ Oyuncu Takımı: " + oyuncu["org"] + "\n ・  Oyuncu KDA: " + oyuncu["kill_deaths"] + "\n ・  Ortlama Raund Hasarı: " + oyuncu["average_damage_per_round"] + 
        "\n ・  Ortlama Raund Asisti: "+ oyuncu["assists_per_round"] + "\n ・ Headshot Yüzdesi : " + oyuncu["headshot_percentage"] + "\n ・ Clutch Başarı Yüzdesi : " + oyuncu["clutch_success_percentage"] +
        "\n ・ İlk Kan Oranı: " + oyuncu["first_kills_per_round"] + "\n ・ İlk Ölme Oranı : " + oyuncu["first_deaths_per_round"],
        color = discord.Color.random()
    ) 
            embed.add_field(name='Oyuncu Profili' ,value=f'[Oyuncu Profili İçin Tıkla](https://www.vlr.gg/search/?q={isim})', inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/954724771034198036/957238194917736459/image.gif"),
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/748960804610768947/957300083756527656/logo.png")
            await ctx.send(embed=embed)
            break
        break


########### STAT AP
class statsystemeu:
    @client.command(aliases=["istatistik-ap"])
    async def statpa(ctx, oyuncu_adı):
        response = requests.get("https://vlrggapi.herokuapp.com/stats/ap")
        json_data = json.loads(response.text)
        oyuncular = []
        for dict in json_data["data"]["segments"]:
            for dict in json_data["data"]["segments"]:
                oyuncular.append(dict)
            isim = oyuncu_adı
        for oyuncu in oyuncular:
         if oyuncu["player"] == isim:
            embed = discord.Embed(
        title = "Oyuncu Adı: " + oyuncu["player"],
        description = "・ Oyuncu Takımı: " + oyuncu["org"] + "\n ・  Oyuncu KDA: " + oyuncu["kill_deaths"] + "\n ・  Ortlama Raund Hasarı: " + oyuncu["average_damage_per_round"] + 
        "\n ・  Ortlama Raund Asisti: "+ oyuncu["assists_per_round"] + "\n ・ Headshot Yüzdesi : " + oyuncu["headshot_percentage"] + "\n ・ Clutch Başarı Yüzdesi : " + oyuncu["clutch_success_percentage"] +
        "\n ・ İlk Kan Oranı: " + oyuncu["first_kills_per_round"] + "\n ・ İlk Ölme Oranı : " + oyuncu["first_deaths_per_round"],
        color = discord.Color.random()
    ) 
            embed.add_field(name='Oyuncu Profili' ,value=f'[Oyuncu Profili İçin Tıkla](https://www.vlr.gg/search/?q={isim})', inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/954724771034198036/957238194917736459/image.gif"),
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/748960804610768947/957300083756527656/logo.png")
            await ctx.send(embed=embed)
            break
###########

##################################################################################################### HABERLER
class haberler:
    @client.command(name="haberler")
    async def ranklar(ctx,):
       response = requests.get("https://vlrggapi.herokuapp.com/news")
       json_data = json.loads(response.text)
       for haber in json_data["data"]["segments"]:
           haberler.url_path = haber["url_path"]
           embed = discord.Embed(
               title = haber["title"],
               description = "・ Açıklama: " + haber["description"] + "\n \n ・ Tarih: " + haber["date"] + "\n \n ・  Yazan: " + haber["author"],
               color = discord.Color.random() 
           )
           
           embed.add_field(name='Haber Detayı' ,value=f'[Detaylı Bilgi İçin Tıkla](https://www.vlr.gg{haberler.url_path})', inline=False)
           embed.set_image(url="https://cdn.discordapp.com/attachments/954724771034198036/957238194917736459/image.gif")
           await ctx.send(embed=embed)
           break

#####################################################################################################

##################################################################################################### /HABERLER
@slash.slash(name="haberler", description="En son yayınlanan haberi gösterir",)
async def slashpa(ctx:SlashContext):
    await ctx.defer("Bot Düşünüyor")
    response = requests.get("https://vlrggapi.herokuapp.com/news")
    json_data = json.loads(response.text)
    for haber in json_data["data"]["segments"]:
           haberler.url_path = haber["url_path"]
           embed = discord.Embed(
               title = haber["title"],
               description = "**・ Açıklama: **" + haber["description"] + "\n \n **・ Tarih: **" + haber["date"] + "\n \n **・  Yazan: **" + haber["author"],
               color = discord.Color.random() 
           )
           
           embed.add_field(name='Haber Detayı' ,value=f'[Detaylı Bilgi İçin Tıkla](https://www.vlr.gg{haberler.url_path})', inline=False)
           embed.set_image(url="https://cdn.discordapp.com/attachments/954724771034198036/957238194917736459/image.gif")
           await ctx.send(embed=embed)
           break

#####################################################################################################

########### YARDIM KOMUTU
class yardım:
    @client.command(name="yardım")
    async def yardım(ctx):
        embed = discord.Embed(
            title = "Valorant Daily Yardım Menüsü",
            description = "**・ İstatistik komutları nasıl kullanılır :** prefixin veya / komutunun ardından istatistik-``na``, ``eu``, ``ap`` ``<oyuncu adı>`` yazılır ve bot size oyuncunun son maçındaki istatisliklerini gösterir.\n \n" + 
            "**・ Örnek Kullanım:** ``!istatistik-na TenZ`` Veya ``/istatistik-na TenZ`` (Bot büyük-küçük harfe duyarlıdır oyuncu adını doğru yazdığınızdan emin olun.).\n \n" +  
            "**・ En Son Yayınlan Haber Nasıl Öğrenilir: ** prefixin veya / komutunun ardından haberler yazılır ve bot size en son yayınlanan haberin bilgilerini gösterir (Haber detayları ingilizcedir.)\n \n" +
            "**・ Örnek Kullanım: ** ``!haberler`` veya ``/haberler``",
            color = discord.Color.blue()
        )

        embed.add_field(name='Destek Sunucum' ,value=f'[Destek Sunucuma Gitmek İçin Tıkla](https://discord.gg/2VBuqq36mC)', inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/954724771034198036/957238194917736459/image.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/748960804610768947/957300083756527656/logo.png")
        await ctx.send(embed=embed)
##############

############## /YARDIM       
@slash.slash(name="yardım", description="Komutlar hakkında bilgi verir",)   
async def slashyardım(ctx:SlashContext):
    await ctx.defer("Bot Düşünüyor")
    embed = discord.Embed(
            title = "Valorant Daily Yardım Menüsü",
            description = "**・ İstatistik komutları nasıl kullanılır :** prefixin veya / komutunun ardından istatistik-``na``, ``eu``, ``ap`` ``<oyuncu adı>`` yazılır ve bot size oyuncunun son maçındaki istatisliklerini gösterir.\n \n" + 
            "**・ Örnek Kullanım:** ``!istatistik-na TenZ`` Veya ``/istatistik-na TenZ`` (Bot büyük-küçük harfe duyarlıdır oyuncu adını doğru yazdığınızdan emin olun.).\n \n" +  
            "**・ En Son Yayınlan Haber Nasıl Öğrenilir: ** prefixin veya / komutunun ardından haberler yazılır ve bot size en son yayınlanan haberin bilgilerini gösterir (Haber detayları ingilizcedir.)\n \n" +
            "**・ Örnek Kullanım: ** ``!haberler`` veya ``/haberler``",
            color = discord.Color.blue()
        )

    embed.add_field(name='Destek Sunucum' ,value=f'[Destek Sunucuma Gitmek İçin Tıkla](https://discord.gg/2VBuqq36mC)', inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/954724771034198036/957238194917736459/image.gif")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/748960804610768947/957300083756527656/logo.png")
    await ctx.send(embed=embed)


@client.event
async def on_ready():
    print(client.user.name)
    await client.change_presence(activity=discord.Game(name="Safe Code <3 LEO4BEY")) 

client.run(token)

#LEO4BEY TARAFINDAN YAZILMIŞTIR İZİNSİZ PAYLAŞILMASI YASAKTIR