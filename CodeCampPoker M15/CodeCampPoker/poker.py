'''implementation of POKER GAME'''
T_RESULT = {}
id_ranking = '--23456789TJQKA'
list_ranking = [i for i in id_ranking]
def kind(hand):
    '''checking the freqency or kind of a hand'''
    return list(map(hand.count, hand))
def max_rank(rank, tie):
    ''' finding the winner for the game'''
    result_list = [[list_ranking.index(num) for num, face in card] for card in tie]

    result_list = list(map(sorted, result_list))

    kind_freq = list(map(kind, result_list))

    if rank == 9:
        max_val = [result_list[index][4] for index in range(len(tie))]
        result = max_val.index(max(max_val))
        return tie[result]
    ti_f = [max(index) for index in kind_freq]
    id_f = [kind_freq[ix].index(ti_f[ix]) for ix in range(len(ti_f)) if ti_f[ix] in kind_freq[ix]]
    res_f = [result_list[idx][id_f[idx]] for idx in range(len(result_list))]
    res = res_f.index(max(res_f))
    return tie[res]
def add_result(rank, hand):
    ''' adding hands to dictonary of same kind'''
    # global T_RESULT
    if rank in T_RESULT:
        T_RESULT[rank].append(hand)
    else:
        T_RESULT[rank] = [hand]
def is_high_card(hand):
    ''' checking for a high kind'''
    list_ = []
    for num, _ in hand:
        list_.append(num)
    set_ = set(list_)
    return len(set_) == 5

def is_fiveofa_kind(hand):
    ''' checking for a five of kind'''
    list_ = []
    for num, _ in hand:
        list_.append(num)
    set_ = set(list_)
    return len(set_) == 1

def is_fourofa_kind(hand):
    ''' checking for a four of kind'''
    list_ = []
    for num, _ in hand:
        list_.append(num)
    set_ = set(list_)
    return len(set_) == 2

def is_threeofa_kind(hand):
    ''' checking for a three of kind'''
    list_ = []
    for num, _ in hand:
        list_.append(num)
    set_ = set(list_)
    return len(set_) == 3

def is_one_pair(hand):
    ''' checking for one pair'''
    list_ = []
    for num, _ in hand:
        list_.append(num)
    set_ = set(list_)
    return len(set_) == 4


def is_fullhouse(hand):
    ''' checking for full house (if it is both three kind and one pair)'''
    return is_threeofa_kind(hand) and is_one_pair(hand)

def is_two_pair(hand):
    ''' checking for two pair'''
    list_ = []
    for num, _ in hand:
        list_.append(num)
    set_ = set(list_)
    return len(set_) == 3

def is_straight(hand):
    ''' checking for straight'''
    # global list_ranking
    f_list = []
    for num, _ in hand:
        f_list.append(list_ranking.index(num))
    f_set = set(f_list)
    return max(f_set)-min(f_set) == 4

def is_flush(hand):
    ''' checking for flush'''
    list_ = []
    for _, suite in hand:
        list_.append(suite)

    set_ = set(list_)
    return len(set_) == 1

def hand_rank(hand):
    ''' finding the rand of each hand'''
    if is_fiveofa_kind(hand):
        add_result(0, hand)
        return 0
    if is_straight(hand) and is_flush(hand):
        add_result(1, hand)
        return 1
    if is_fourofa_kind(hand) and not is_fullhouse(hand):
        add_result(2, hand)
        return 2
    if is_fullhouse(hand) and not is_fourofa_kind(hand):
        add_result(3, hand)
        return 3
    if is_flush(hand):
        add_result(4, hand)
        return 4
    if is_straight(hand):
        add_result(5, hand)
        return 5
    if is_threeofa_kind(hand):
        add_result(6, hand)
        return 6
    if is_two_pair(hand):
        add_result(7, hand)
        return 7
    if is_one_pair(hand):
        add_result(8, hand)
        return 8
    if is_high_card(hand):
        add_result(9, hand)
        return 9

def poker(hands):
    '''initiating poker game'''
    list(map(hand_rank, hands))
    return 0
if __name__ == "__main__":
    COUNT = int(input())
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    poker(HANDS)
    p_game, high_rank_list = min(T_RESULT), T_RESULT[min(T_RESULT)]
    if len(high_rank_list) == 1:
        print(" ".join(high_rank_list[0]))
    else:
        print(" ".join(max_rank(p_game, high_rank_list)))
