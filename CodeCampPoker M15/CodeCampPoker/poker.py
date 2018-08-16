result = {}
ranking = '--23456789TJQKA'
ranking_list = [i for i in ranking]
# tie_breaker= {0:5,1:5,2:4,3:3,4:1,5:5,6:3,7:2,8:2,9:5}
def max_rank(rank,tie):
	tie_ = []
	for i in range(len(tie)):
		tie_.append(tuple(rank,tuple(tie(i))))

	return tie[index(max(tuple(tie_)))]




	# result_list = []
	# if rank == 4:
	# 	for card in tie:
	# 		rank_list = []
	# 		for num,face in card:
	# 			rank_list.append(ranking.index(num))
	# 		result_list.append(rank_list)
	# 	ans_list = [max(maximum) for maximum in result_list]
	# 	result = ans_list.index(max(ans_list))
	# 	return tie[result]

	# for card in tie:
	# 	rank_list = []
	# 	for num,face in card:
	# 		rank_list.append(num)
	# 	result_list.append(rank_list)

	# set_list = []
	# for i in result_list:
	# 	set_list.append(set(i))

	# m = []
	# # max_count = 0
	# for i in range(len(set_list)):
	# 	for j in set_list[i]:
	# 		if result_list.count(j) == tie_breaker[rank]:
	# 			m.append()

	# max_count = max(m)
	# for i in range(len(result_list)):
	# 	if max_count in result_list[i]:
	# 		return tie[i]


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
	return is_threeofa_kind(hand) and is_two_pair(hand)

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
	# print(poker(HANDS))
	poker(HANDS)
	# print(result)
	game,high_rank_list = min(result),result[min(result)]
	if len(high_rank_list) == 1:
		print(" ".join(high_rank_list[0]))
	else:
		print(" ".join(max_rank(game,high_rank_list)))
	# print(high_rank_list)
