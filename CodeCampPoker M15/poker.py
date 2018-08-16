'''
	Write a program to evaluate poker hands and determine the winner
	Read about poker hands here.
	https://en.wikipedia.org/wiki/List_of_poker_hands
'''
result = {}
ranking = '0023456789TJQKA'
ranking_list = [int(i) for i in ranking]
def add_result(rank,hand):
	global result
	if rank in result:
		result[rank].append(hand)
	else:
		result[rank] = [hand]
def is_high_card(hand):

def is_fiveofa_kind(hand):
	list_ =[]
	for num,suite in hand:
		list_.append(num)
	set_ = set(list_)
	return len(set_)==1


def is_fourofa_kind(hand):
	list_ =[]
	for num,suite in hand:
		list_.append(num)
	set_ = set(list_)
	return len(set_)==2

def is_threeofa_kind(hand):
	list_ =[]
	for num,suite in hand:
		list_.append(num)
	set_ = set(list_)
	return len(set_)==3


def is_one_pair(hand):
	list_ =[]
	for num,suite in hand:
		list_.append(num)
	set_ = set(list_)
	return len(set_)==4
	

def is_fullhouse(hand):
	return is_threeofa_kind(hand) and is_two_pair(hand)

def is_two_pair(hand):
	list_ =[]
	for num,suite in hand:
		list_.append(num)
	set_ = set(list_)
	return len(set_)==3





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
	global ranking_list
	list_ = []
	for num,suite in hand:
		list_.append(ranking_list.index(num))

	set_ = set(list_)
	return len(set_)==5 and max(set_)-min(set_)==4

def is_flush(hand):
	'''
		How do we find out if the given hand is a flush?
		The hand has a list of cards represented as strings.
		Do we need both the characters in the string? No.
		The second character is good enough to determine a flush
		Think of an algorithm: given the card suite how to check if it is a flush
		Write the code for it and return True if it is a flush else return False
	'''
	list_ = []
	for num,suite in hand:
		list_.append(suite)
	
	set_ = set(list_)
	return len(set_) == 1
	

def hand_rank(hand):
	if is_fiveofa_kind(hand):
		add_result(0,hand):return 0
	if is_straight(hand) and is_flush(hand):
		add_result(1,hand);return 1
	if is_fourofa_kind(hand):
		add_result(2,hand);return 2
	if is_fullhouse(hand):
		add_result(3,hand);return 3
	if is_flush(hand):
		add_result(4,hand);return 4
	if is_straight(hand):
		add_result(5,hand);return 5
	if is_threeofa_kind(hand):
		add_result(6,hand);return 6
	if is_two_pair(hand):
		add_result(7,hand);return 7
	if is_one_pair(hand):
		add_result(8,hand);return 8
	if is_high_card(hand):
		add_result(9,hand);return 9
	add_result(10,hand);return 10

	
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
	res = list(map(hand_rank,hands))
	# return min(hands, key=hand_rank)

if __name__ == "__main__":
	# read the number of test cases
	COUNT = int(input())
	# iterate through the test cases to set up hands list
	HANDS = []
	for x in range(COUNT):
		line = input()
		ha = line.split(" ")
		HANDS.append(ha)
	# print(HANDS)
	# test the poker function to see how it works
	print(' '.join(poker(HANDS)))
