import json
import os
import time
import random


BOOSTER_SIZE = 5
SECRET_FREQ = 24
ULTRA_FREQ = 12
SUPER_FREQ = 5
RARE_FREQ = 1


cardCollectionFileName = './cardCollection.json'

try:
	with open(cardCollectionFileName) as collection_file:
		collection = json.load(collection_file)
except:
	newCollection = {'cards':[]}
	with open(cardCollectionFileName, 'w') as json_file:
		json.dump(newCollection, json_file)
	collection = newCollection

for i in collection['cards']:
	print(i)


#load in the booster pack data
with open('./boosterData.json') as json_file:
	data = json.load(json_file)




while True:
	os.system('cls')
	print('Available booster packs:')
	time.sleep(1)
	nameList = []
	for i, boosterPackName in enumerate(data):
		print('({n}) {b}'.format(n=i+1, b=boosterPackName))
		nameList.append(boosterPackName)

	selectedPack = input('Please enter the number corresponding to the desired booster pack:\n==> ')

	if selectedPack.lower() == 'exit':
		exit()
	else:
		if selectedPack.isdigit():
			selectedPack = int(selectedPack)

	if type(selectedPack) != int or selectedPack < 1 or selectedPack > len(data):
		print('Incorrect pack ID entered!')
		continue
	else:
		boosterPackName = nameList[selectedPack-1]
		newCardNames = []
		os.system('cls')

		print('Opening booster pack {n}'.format(n=boosterPackName.upper()))
		time.sleep(3)
		for cardNumber in range(0 ,BOOSTER_SIZE):
			print('Drawing card #{n}'.format(n=cardNumber+1))
			if cardNumber+1 != BOOSTER_SIZE:
				#choose a common card
				cardRarity = 'common'
				time.sleep(1)
			else:
				time.sleep(3)
				if random.randrange(0,SECRET_FREQ) == 0:
					cardRarity = 'secret'
				elif random.randrange(0,ULTRA_FREQ) == 0:
					cardRarity = 'ultra'
				elif random.randrange(0,SUPER_FREQ) == 0:
					cardRarity = 'super'
				elif random.randrange(0,RARE_FREQ) == 0:
					cardRarity = 'rare'
				else:
					cardRarity = 'common'

			newCard = random.choice(data[boosterPackName][cardRarity]).upper()
			newCardNames.append(newCard)
			print('({r}): {n}\n'.format(n=newCard, r=cardRarity.upper()))
			time.sleep(1)

	for cardName in newCardNames:
		if collection['cards'].count(cardName) < 3:
			collection['cards'].append(cardName.upper())
	collection['cards'].sort()
	#save everything
	with open(cardCollectionFileName, 'w') as json_file:
		json.dump(collection, json_file)
	pause = input('\n\n\nPress ENTER to continue.')



