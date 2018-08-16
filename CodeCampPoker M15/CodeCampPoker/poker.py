result = {}
ranking = '--23456789TJQKA'
ranking_list = [i for i in ranking]


def kind(li):
	# s = set(li)
	# print(s)
	return list(map(li.count,li))

def max_rank(rank,tie):
	result_list = []
	for card in tie:
		rank_list = []
		for num,face in card:
			rank_list.append(ranking.index(num))
		result_list.append(rank_list)
	result_list = list(map(sorted,result_list))
	rl = list(map(kind,result_list))
	if rank == 9:
		ll = [len(set(i))==1 for i in rl]
		lll = list(set(ll))
		lll1 = []
		if lll[0]:
			for i in range(len(tie)):
				lll1.append(result_list[i][4])
		m1 = lll1.index(max(lll1))
		return tie[m1]

	l1 = [max(i) for i in rl]
	l2 = []
	for i in range(len(l1)):
		if l1[i] in l[i]:
			l2.append(l[i].index(l1[i]))
	print(l2,"l2") 
	l3=[]
	for i in range(len(result_list)):
		l3.append(result_list[i][l2[i]])
	m = l3.index(max(l3))
	return tie[m]
def add_result(rank,hand):
	global result
	if rank in result:
		result[rank].append(hand)
	else:
		result[rank] = [hand]
def is_high_card(hand):
	list_ =[]
	for num,suite in hand:
		list_.append(num)
	set_ = set(list_)
	return len(set_)==5

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
	return is_threeofa_kind(hand) and is_one_pair(hand)

def is_two_pair(hand):
	list_ =[]
	for num,suite in hand:
		list_.append(num)
	set_ = set(list_)
	return len(set_)==3

def is_straight(hand):
	global ranking_list
	list_F = []
	for num,suite in hand:
		list_F.append(ranking_list.index(num))
	set_F = set(list_F)
	return max(set_F)-min(set_F)==4

def is_flush(hand):
	list_ = []
	for num,suite in hand:
		list_.append(suite)
	
	set_ = set(list_)
	return len(set_) == 1

def hand_rank(hand):
	if is_fiveofa_kind(hand):
		add_result(0,hand);return 0
	if is_straight(hand) and is_flush(hand):
		add_result(1,hand);return 1
	if is_fourofa_kind(hand) and not(is_fullhouse(hand)):
		add_result(2,hand);return 2
	if is_fullhouse(hand) and not(is_fourofa_kind(hand)):
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
	
def poker(hands):
	res = list(map(hand_rank,hands))
	# print(res)
	return 0
if __name__ == "__main__":
	COUNT = int(input())
	HANDS = []
	for x in range(COUNT):
		line = input()
		ha = line.split(" ")
		HANDS.append(ha)
	poker(HANDS)
	# print(result)
	game,high_rank_list = min(result),result[min(result)]
	if len(high_rank_list) == 1:
		print(" ".join(high_rank_list[0]))
	else:
		print(" ".join(max_rank(game,high_rank_list)))

