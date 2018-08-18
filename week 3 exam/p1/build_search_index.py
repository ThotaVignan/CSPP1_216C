'''program to searching base on index'''
import re

def load_stopwords(filename):
    ''' loads stop words from a file and returns a dictionary '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords

def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    stop_words = load_stopwords('stopwords.txt')
    text = text.lower().split(' ')
    text = [re.sub('[^a-z]', '', word).strip() for word in text]
    text = [word for word in text if word not in stop_words and len(word) > 0]
    return text

def build_search_index(docs):
    ''' Process the docs step by step as given below '''
    dictonary = {}
    docs = list(map(word_list, docs))
    for count, l_index in enumerate(docs, 0):
        dic = {}
        for e_index in l_index:
            if e_index not in dic:
                dic[e_index] = [count, 1]
            else:
                dic[e_index][1] += 1
        # print(dic)
        for data in dic:
            if data not in dictonary:
                dictonary[data] = [tuple(dic[data])]
            else:
                dictonary[data].append(tuple(dic[data]))

    return dictonary



    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for _ in range(lines):
        documents.append(input())
        # i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
