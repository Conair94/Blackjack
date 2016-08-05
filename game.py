import random
import console
n=-1
end=0
player_hand=[]
deck=[]
dealer_hand=[]

def hit():
	player_hand.insert(0,deck[0])
	deck.remove(player_hand[0])
	console.clear()
	print('Dealer has '+str(dealer_hand[0]))
	print('')
	print('You drew a '+ str(player_hand[0]))
	print(player_hand)
	print('')

def deal():
	player_hand=[]
	dealer_hand=[]
	dealer_hand.insert(0,deck[0])
	deck.remove(dealer_hand[0])
	dealer_hand.insert(0,deck[0])
	deck.remove(dealer_hand[0])
	player_hand.insert(0,deck[0])
	deck.remove(player_hand[0])
	player_hand.insert(0,deck[0])
	deck.remove(player_hand[0])
	play()
	
def dealer_turn():
	console.clear()
	print('Dealer has '+str(dealer_hand))
	print('')
	print('You have '+ str(player_hand))
	while sum(dealer_hand) <=16:
		print('Dealer hits')
		dealer_hand.insert(0,deck[0])
		deck.remove(dealer_hand[0])
		print('Dealer draws a '+ str(dealer_hand[0]))
		print('Dealer has '+ str(dealer_hand))
		print('')
		if sum(dealer_hand) >=21:
			print('Dealer busts')
	if sum(dealer_hand) <= sum(player_hand):
		print('Dealer loses')
		end()
	else :
		print('Dealer wins')
		end()

def play():
	print('Dealer has '+str(dealer_hand[0]))
	print('')
	print('You have '+str(player_hand))
	if sum(dealer_hand) ==21:
		print('Dealer has blackjack'+str(dealer_hand))
		if sum(player_hand) ==21:
			print('You also have blackjack')
			print('The hand is pushed')
			end()
		else:
			print('You dont have blackjack')
			print("you fucking loser,")
			print("this is why you are a hopeless maggot")
			print("living in your parent's basement")
			end()
	elif sum(dealer_hand) <=21:
		if sum(player_hand) ==21:
			print('You win!')
			end=1
	usr_input = ''
	end=0
	while usr_input not in ['stay']:
		usr_input=raw_input('hit or stay?')
		if sum(player_hand) >=21:
			bust_counter=1
			print('You bust')
			end()
		elif usr_input =='hit':
			hit()
		elif usr_input =='stay':
			dealer_turn()
			
def end():
	while usr_input not in ['yes']:
		usr_input=raw_input('Hand over, deal a new hand from same deck?')
		if usr_input == 'yes':
			play()
		else:
			usr_input=raw_input('Deal new deck?')
			if usr_input == 'yes':
				deck_creation()
			else:
				usr_input=raw_input('Quit?')
		

console.clear()
print('Welcome to Black jack by Connor Lockhart')
print('')

def deck_creation():
	n=-1
	deck=[]
	while n <=0:
		print('Number of decks must be a positive integer')
		try:
			n=int(raw_input('How many decks: '))
		except:
			print ("Do you think you're clever?")
	deck= n*4*[2,3,4,5,6,7,8,9,10,10,10,10,11]
	random.shuffle(deck)
	deal()
deck_creation()
