import discord
import requests
import json
import random

client = discord.Client()



def get_quote():
    response=requests.get("https://zenquotes.io/api/random")
    x=json.loads(response.text)
    q=x[0]['q']+"-"+x[0]['a']
    return(q)

def get_anime_quote():
    response=requests.get("https://animechan.vercel.app/api/random")
    x=json.loads(response.text)
    q=x['quote']+"-"+x['anime']
    #print(q1)
    return(q)

def get_daily_quote():
    response=requests.get("https://zenquotes.io/api/today")
    x2=json.loads(response.text)
    q2=x2[0]['q']+"-"+x2[0]['a']
    return(q2)   

def getFriendsQuote():
    response=requests.get("https://friends-quotes-api.herokuapp.com/quotes/random")
    x3=json.loads(response.text)
    q3=x3['quote']+" -"+x3['character']
    return(q3)         
 

sadWords=["sad","depressed","unhappy","melancholy","gloomy","pissed"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!"
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #using random apis
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$quote'):
        quote=get_quote()
        await message.channel.send(quote)  

    if message.content.startswith('$today'):
        quote2=get_daily_quote()
        await message.channel.send(quote2)

    if message.content.startswith('$friends'):
        friendsQuote=getFriendsQuote()
        await message.channel.send(friendsQuote)    
    
    if message.content.startswith('$anime'):
        animequote=get_anime_quote()
        await message.channel.send(animequote)
    
    #looks for 'sad words' in a message and sends an uplifting message in the chat.
    msg=message.content
    if any(word in msg for word in sadWords):
        await message.channel.send(random.choice(starter_encouragements))




client.run(
    # add your key here
    )