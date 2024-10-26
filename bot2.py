import discord
from discord.ext import commands
from bot_logic import *
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def haslo(ctx, pass_lenght = 10):
    await ctx.send(gen_pass(pass_lenght))

@bot.command()
async def pomysly(ctx):
    pomysly = ["Ramki na zdjęcia z patyczków po lodach", "Pojemniki na długopisy z rolek po papierze toaletowym", "Świeczniki ze słoików", "Łańcuch z kolorowego papieru", 
                "Ozdoby z masy solnej", "Breloczki z koralików i żyłki", "Doniczki z puszek po konserwach", "Ozdobne zakładki do książek", "Kolorowe mozaiki z potłuczonych płytek lub szkła",
                "Organizer na biżuterię z kartonów po jajkach", "Ozdobne świece z resztek świec", "Kolorowe pompony z włóczki", "Torebki na prezenty z gazet lub starego papieru",
                "Podstawki pod kubki z korków po winie", "Dywanik z pomponów", "Witraż z plastikowych butelek", "Lampiony z papieru", "Torba z koszulki", "Kolorowe śnieżynki z papieru",
                "Kwiaty z filtrów do kawy", "Zegary z płyt winylowych", "Szkatułki z kartonowych pudełek", "Poduszki z jeansu", "Podkładki pod talerze z płyt CD",
                "Ptaszki z filcu", "Zakładki do książek z kartonu i tasiemek", "Girlandy z kolorowego papieru", "Ozdobne słoiki na przybory", "Składane miseczki z papieru",
                "Latawce z plastikowych torebek", "Kolaże z gazet i czasopism", "Piórniki z opakowań po chusteczkach", "Malowane kamienie", "Ozdoby świąteczne z masy solnej",
                "Dzwonki wietrzne z muszelek"]
    await ctx.send(random.choice(pomysly))

bot.run("")
