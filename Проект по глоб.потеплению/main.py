import discord
from discord.ext import commands
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io

intents = discord.Intents.default()
intents.message_content = True

def generate_climate_data():
    years = np.arange(1900, 2024)
    temperatures = np.random.uniform(low=-40.0, high=40.0, size=len(years))
    data = pd.DataFrame({'Год': years, 'Температура': temperatures})
    return data

def visualize_data():
    data = generate_climate_data()
    
    plt.figure(figsize=(10, 6))
    plt.plot(data['Год'], data['Температура'], marker='o')
    plt.title('Изменения температуры с годами')
    plt.xlabel('Год')
    plt.ylabel('Температура')
    plt.grid(True)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    
    return buf

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.command()
async def visualize(ctx):
    chart = visualize_data()
    await ctx.send(file=discord.File(chart, 'climate_data.png'))

bot.run('')
