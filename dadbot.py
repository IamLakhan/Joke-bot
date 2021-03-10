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
	url = 'https://api.rootnet.in/covid19-in/stats/latest'
	response = requests.get(url, headers = {'Accept': 'application/json'})
	data = response.json() 
	total = data['data']['summary']['total']
	death = data['data']['summary']['deaths']
	recover = data['data']['summary']['discharged']
	active = total - recover - death
	return (f"Total cases : {total} \nDeaths: {death} \nRecovered : {recover} \nActive: {active} \nLast Updated: {data['lastRefreshed']}")

def insults():
	url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
	response = requests.get(url, headers = {'Accept': 'application/json'})
	data = response.json()
	return str((data['insult']))

@bot.event
async def on_ready():
	print("Let's go!")

@bot.event
async def on_message(message):
	channel = message.channel
	content = message.content
	if content == '!joke':
		joke = tell_joke()
		await channel.send(joke)
	
	if content.lower() == 'go corona':
		await channel.send('Corona Go!')

	if content == '!meme':
		meme = get_meme()
		await channel.send(meme)
		
	if content == '!corona':
		update = get_corona_update()
		await channel.send(update)
	
	if content == '!insult':
		insult = insults()
		await channel.send(insult)
		
bot.run(TOKEN)
