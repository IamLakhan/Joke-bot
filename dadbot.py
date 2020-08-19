import discord
from discord.ext import commands
import os
import requests

TOKEN = '' # Paste token here

bot = commands.Bot(command_prefix = '.')

def tell_joke():
	url = 'https://icanhazdadjoke.com/'
	response = requests.get(url, headers={"Accept": "application/json"})
	data = response.json()
	return str(data['joke'])

def get_meme():
	url = 'https://meme-api.herokuapp.com/gimme'
	response = requests.get(url, headers={"Accept": "application/json"})
	data = response.json()
	return str((data['url']))

def get_corona_update():
	url = 'https://api.covid19india.org/data.json?'
	response = requests.get(url)
	data = response.json()
	active = str(int(data["statewise"][0]["active"]))
	confirmed = str(int(data["statewise"][0]["confirmed"]))
	deaths =  str(int(data["statewise"][0]["deaths"]))
	message = "Cofirmed cases:" + confirmed + "active:" + active + "deaths:" + deaths
	return(str(message))

@bot.event
async def on_ready():
	print("Let's go!")

@bot.event
async def on_message(message):
	channel = message.channel
	content = message.content
	if content == '.joke':
		joke = tell_joke()
		await channel.send(joke)
	
	if content.lower() == 'go corona':
		await channel.send('Corona Go!')

	if content == '.meme':
		meme = get_meme()
		await channel.send(meme)
		
	if content == '.corona':
		update = get_corona_update()
		await channel.send(update)
		
		

bot.run(TOKEN)

