''' Programm to find the similarity of content between two files'''
import re
import math

def calculations(dictonary):
    num = 0
    de1 = 0
    de2 = 0
    for d in dictonary:
        num+=dictonary[d][0]*dictonary[d][1]
    for d in dictonary:
        de1+=dictonary[d][0]**2
    for d in dictonary:
        de2+=dictonary[d][1]**2  
    return num/(math.sqrt(de1)*math.sqrt(de2) )

def tokens(data):
    data = data.lower()
    data = re.sub('[^a-z\ ]', '',data)
    # print(data)
    s_words = load_stopwords("stopwords.txt")
    data = data.strip().split(" ")
    # print(data)
    list1 = []
    # print(s_words)
    for word in data:
        # k = re.sub('[^a-z\ ]','',word)
        if word not in s_words and len(word)>0:
            list1.append(word)
    return list1


def freq(dictonary,data,index):

    for d in data:
        if d not in dictonary:
            dictonary[d] = [0,0]
            dictonary[d][index]+=1
        else:
            dictonary[d][index]+=1
    return dictonary



def similarity(dict1, dict2):
    '''Compute the document distance as given in the PDF'''
    dictonary = {}
    dict1 = tokens(dict1)
    dict2 = tokens(dict2)
    dictonary = freq(dictonary,dict1,0)
    dictonary = freq(dictonary,dict2,1)
    # print(dict1+dict2)
    # print(dict1+dict2.count("we've"))
    

    result = calculations(dictonary)
    return result




def load_stopwords(filename):
    '''loads stop words from a file and returns a dictionary'''
    stopwords = []
    with open(filename, 'r') as file:
        for line in file:
            stopwords.append(line.strip())
    return stopwords

def main():
    '''take two inputs and call the similarity function'''
    input1 = input()
    input2 = input()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
