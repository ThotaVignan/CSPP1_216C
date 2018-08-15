'''
	Write a program to evaluate poker hands and determine the winner
	Read about poker hands here.
	https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def is_fourofa_kind(hand):
	length = len(hand)
	newhandvalues = []
	for i in range(length):
		if hand[i][0] == 'A':
			newhandvalues.append(14)
		elif hand[i][0] == 'K':
			newhandvalues.append(13)
		elif hand[i][0] == 'Q':
			newhandvalues.append(12)
		elif hand[i][0] == 'J':
			newhandvalues.append(11)
		elif hand[i][0] == 'T':
			newhandvalues.append(10)
		else:
			newhandvalues.append(int(hand[i][0]))
	newhandvalues.sort()
	for i in range(2):
		if newhandvalues[i] == newhandvalues[i+1] == newhandvalues[i+2] == newhandvalues[i+3]:
			return True
	return False

def is_threeofa_kind(hand):
	length = len(hand)
	newhandvalues = []
	for i in range(length):
		if hand[i][0] == 'A':
			newhandvalues.append(14)
		elif hand[i][0] == 'K':
			newhandvalues.append(13)
		elif hand[i][0] == 'Q':
			newhandvalues.append(12)
		elif hand[i][0] == 'J':
			newhandvalues.append(11)
		elif hand[i][0] == 'T':
			newhandvalues.append(10)
		else:
			newhandvalues.append(int(hand[i][0]))
	newhandvalues.sort()
	for i in range(length-3):
		if newhandvalues[i] == newhandvalues[i+1] == newhandvalues[i+2]:
			return True
	return False

def is_one_pair(hand):
	length = len(hand)
	newhandvalues = []
	for i in range(length):
		if hand[i][0] == 'A':
			newhandvalues.append(14)
		elif hand[i][0] == 'K':
			newhandvalues.append(13)
		elif hand[i][0] == 'Q':
			newhandvalues.append(12)
		elif hand[i][0] == 'J':
			newhandvalues.append(11)
		elif hand[i][0] == 'T':
			newhandvalues.append(10)
		else:
			newhandvalues.append(int(hand[i][0]))
	newhandvalues.sort()

	for i in range(length-1):
		if newhandvalues[i] == newhandvalues[i+1]:
			return True
	return False

def is_fullhouse(hand):
	length = len(hand)
	newhandvalues = []
	for i in range(length):
		if hand[i][0] == 'A':
			newhandvalues.append(14)
		elif hand[i][0] == 'K':
			newhandvalues.append(13)
		elif hand[i][0] == 'Q':
			newhandvalues.append(12)
		elif hand[i][0] == 'J':
			newhandvalues.append(11)
		elif hand[i][0] == 'T':
			newhandvalues.append(10)
		else:
			newhandvalues.append(int(hand[i][0]))
	newhandvalues.sort()
	count_ = []
	# print(len(count_),"count ==")
	for i in range(5):
		# print(i)
		count_.append(newhandvalues.count(newhandvalues[i]))
		# print(count_)
	if 3 in count_:
		if 2 in count_:
			return True
	return False






def is_two_pair(hand):
	length = len(hand)
	newhandvalues = []
	for i in range(length):
		if hand[i][0] == 'A':
			newhandvalues.append(14)
		elif hand[i][0] == 'K':
			newhandvalues.append(13)
		elif hand[i][0] == 'Q':
			newhandvalues.append(12)
		elif hand[i][0] == 'J':
			newhandvalues.append(11)
		elif hand[i][0] == 'T':
			newhandvalues.append(10)
		else:
			newhandvalues.append(int(hand[i][0]))
	l = set(newhandvalues)
	if len(l) == 3:
		return True
	return False





def is_straight(hand):
	'''
		How do we find out if the given hand is a straight?
		The hand has a list of cards represented as strings.
		There are multiple ways of checking if the hand is a straight.
		Do we need both the characters in the string? No.
		The first character is good enough to determine a straight
		Think of an algorithm: given the card face value how to check if it a straight
		Write the code for it and return True if it is a straight else return False
	'''
	length = len(hand)
	newhandvalues = []
	for i in range(length):
		if hand[i][0] == 'A':
			newhandvalues.append(14)
		elif hand[i][0] == 'K':
			newhandvalues.append(13)
		elif hand[i][0] == 'Q':
			newhandvalues.append(12)
		elif hand[i][0] == 'J':
			newhandvalues.append(11)
		elif hand[i][0] == 'T':
			newhandvalues.append(10)
		else:
			newhandvalues.append(int(hand[i][0]))
	newhandvalues.sort()
	for i in range(length-1):
		if newhandvalues[i+1] - newhandvalues[i] != 1:
			return False
	return True
def is_flush(hand):
	'''
		How do we find out if the given hand is a flush?
		The hand has a list of cards represented as strings.
		Do we need both the characters in the string? No.
		The second character is good enough to determine a flush
		Think of an algorithm: given the card suite how to check if it is a flush
		Write the code for it and return True if it is a flush else return False
	'''
	length = len(hand)
	for i in range(length - 1):
		if hand[i][1] != hand[i+1][1]:
			return False
	return True



def hand_rank(hand):
	'''
		You will code this function. The goal of the function is to
		return a value that max can use to identify the best hand.
		As this function is complex we will progressively develop it.
		The first version should identify if the given hand is a straight
		or a flush or a straight flush.
	'''

	# By now you should have seen the way a card is represented.
	# If you haven't then go the main or poker function and print the hands
	# Each card is coded as a 2 character string. Example Kind of Hearts is KH
	# First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
	# Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
	# What would be the logic to determine if a hand is a straight or flush?
	# Let's not think about the logic in the hand_rank function
	# Instead break it down into two sub functions is_straight and is_flush
	if is_straight(hand) and is_flush(hand):
		return 1
	if is_fourofa_kind(hand):
		return 2
	if is_fullhouse(hand):
		return 3
	if is_flush(hand):
		return 4
	if is_straight(hand):
		return 5
	if is_threeofa_kind(hand):
		return 6
	if is_two_pair(hand):
		return 7
	if is_one_pair(hand):
		return 8
	# check for straight, flush and straight flush
	# best hand of these 3 would be a straight flush with the return value 3
	# the second best would be a flush with the return value 2
	# third would be a straight with the return value 1
	# any other hand would be the fourth best with the return value 0
	# max in poker function uses these return values to select the best hand
	return 9
def poker(hands):
	'''
		This function is completed for you. Read it to learn the code.

		Input: List of 2 or more poker hands
			   Each poker hand is represented as a list
			   Print the hands to see the hand representation

		Output: Return the winning poker hand
	'''

	# the line below may be new to you
	# max function is provided by python library
	# learn how it works, in particular the key argument, from the link
	# https://www.programiz.com/python-programming/methods/built-in/max
	# hand_rank is a function passed to max
	# hand_rank takes a hand and returns its rank
	# max uses the rank returned by hand_rank and returns the best hand
	# max(hands, key=hand_rank)
	return min(hands, key=hand_rank)

if __name__ == "__main__":
	# read the number of test cases
	COUNT = int(input())
	# iterate through the test cases to set up hands list
	HANDS = []
	# for x in range(COUNT):
	while True:
		line = input()
		ha = line.split(" ")
		HANDS.append(ha)
	# print(HANDS)
	# test the poker function to see how it works
	print(' '.join(poker(HANDS)))
