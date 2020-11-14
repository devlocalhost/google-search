import time
import sys
import os
from time import sleep
from googlesearch import search

def kill():
	sleep(0.2)
	sys.exit()

def mainMenu():
	sleep(0.2)
	ask = input('Press enter to continue, or e to exit\n')

	if ask == '':
		sleep(0.2)
		os.system('clear')
		srchgoogle()

	elif ask == 'e':
		sleep(0.2)
		os.system('clear')
		kill()

	else:
		sleep(0.2)
		print(f'Invalid input "{ask}"')
		sleep(1)
		os.system('clear')
		mainMenu()

def srchgoogle():
	sleep(0.2)
	searchres = input('Search for something\n_')
	sleep(0.2)
	resnum = int(input('How many results would you like?\n_'))
	os.system('clear')

	print(f'Results related to "{searchres}":')
	for url in search(searchres, stop=resnum):
		print(f'   {url}')

	skag()

def skag():
	askagain = input('\nSearch again? (yes, no)\n')

	if askagain == 'yes':
		sleep(0.2)
		srchgoogle()

	elif askagain == 'no':
		sleep(0.2)
		os.system('clear')
		kill()

	else:
		sleep(0.2)
		print(f'Invalid input "{askagain}"')
		sleep(1)
		os.system('clear')
		skag()

mainMenu()
