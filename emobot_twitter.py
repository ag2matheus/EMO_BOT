import tweepy
import random as rd
import time

print('emo bot arrived')

CONSUMER_KEY = '5OduZSZR2y08ydStFrBliZi3x'
CONSUMER_SECRET = '70AHRrdsCZZE2ij2JgFIUxyoNvDmgNGpkqKCr8uziQgLD5swMp'
ACCESS_KEY = '1395751977422893056-ptYJdBC8X6R1Vi0d6yvJwRiH9sj3JB'
ACCESS_SECRET = 'RWM3u5u4FUHFuk8WbCwWklhcPiLtneSX5Io2BpDxVTAaq'

from tweepy import OAuthHandler
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#api.update_status('Hello, emo nation!')

from random import choice

def post_tweet():
	#Abrindo o doc com os couples e transformando em lista:
	with open('emo_bot_pairing.txt' , 'r') as g:
		couple = [line.rstrip('\n') for line in g]
		#print(couple)

	#Abrindo o doc com as frases e transformando em lista:
	with open('emo_bot_lyrics.txt' , 'r') as f:
		frase = [line.rstrip('\n') for line in f]
		#print(frase)

	#Sorteando os couples:
	first = rd.choice(couple)
	#print(choice(couple))

	#Sorteando as frases:
	twice = rd.choice(frase)
	#print(choice(frase))

	tweet = first + "\n" + twice
	#+ "\n#HAPPY_SVT_DAY \n#SVT_6th_Anniversary \n#6Years_with_CARAT"

	try:
		api.update_status(tweet)
		print(tweet)
	except tweepy.TweepError as error:
		if error.api_code == 187:
			print('be original')

		else:
			print("batata")

while True:
	post_tweet()
	time.sleep(3600)
