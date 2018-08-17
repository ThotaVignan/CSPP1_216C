'''implementation of POKER GAME'''
T_RESULT = {}
ID_RANKING = '--23456789TJQKA'
LIST_RANKING = [i for i in ID_RANKING]
def kind(hand):
    '''checking the freqency or kind of a hand'''
    return list(map(hand.count, hand))
def max_rank(rank, tie):
    ''' finding the winner for the game'''
    print(rank," --- rank")
    result_list = [[LIST_RANKING.index(num) for num, face in card] for card in tie]
    print(result_list," --- Result List 0")

    result_list = list(map(sorted, result_list))
    print(result_list," --- Result List 1")


    kind_freq = list(map(kind, result_list))
    print(kind_freq," --- Kind freq")

    if rank == 9:
        max_val = [result_list[index][4] for index in range(len(tie))]
        print(max_val," --- Max Val")
        result = max_val.index(max(max_val))
        print(result," --- Result")
        print(tie[result]," --- tie[result]")
        return tie[result]
    ti_f = [max(index) for index in kind_freq]
    print(ti_f," --- ti_f")
    id_f = [kind_freq[ix].index(ti_f[ix]) for ix in range(len(ti_f)) if ti_f[ix] in kind_freq[ix]]
    print(id_f," --- id_f")
    res_f = [result_list[idx][id_f[idx]] for idx in range(len(result_list))]
    print(res_f," --- res_f")
    res = res_f.index(max(res_f))
    print(res," --- res")
    print(tie[res]," --- tie[res]")
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
    # global LIST_RANKING
    f_list = []
    for num, _ in hand:
        f_list.append(LIST_RANKING.index(num))
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
        return 0+2
    if is_straight(hand) and is_flush(hand):
        add_result(1, hand)
        return 1+2
    if is_fourofa_kind(hand) and not is_fullhouse(hand):
        add_result(2, hand)
        return 2+2
    if is_fullhouse(hand) and not is_fourofa_kind(hand):
        add_result(3, hand)
        return 3+2
    if is_flush(hand):
        add_result(4, hand)
        return 4+2
    if is_straight(hand):
        add_result(5, hand)
        return 5+2
    if is_threeofa_kind(hand):
        add_result(6, hand)
        return 6+2
    if is_two_pair(hand):
        add_result(7, hand)
        return 7+2
    if is_one_pair(hand):
        add_result(8, hand)
        return 8+2
    if is_high_card(hand):
        add_result(9, hand)
        return 9+2

def poker(hands):
    '''initiating poker game'''
    list(map(hand_rank, hands))

if __name__ == "__main__":
    COUNT = int(input())
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    poker(HANDS)
    print(T_RESULT)
    GAME, HIGH_RANK_LIST = min(T_RESULT), T_RESULT[min(T_RESULT)]
    print(GAME,HIGH_RANK_LIST)
    if len(HIGH_RANK_LIST) == 1:
        print(" ".join(HIGH_RANK_LIST[0]))
    else:
        print(" ".join(max_rank(GAME, HIGH_RANK_LIST)))
