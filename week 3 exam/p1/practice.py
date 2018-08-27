import re
def print_search_index(index):
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])


def load_stopwords(filename):
    ''' loads stop words from a file and returns a dictionary '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords

def filtering(words):
    words = words.lower().split(' ')
    # words1 = []
    # for letters in words:
    #     words1.append(re.sub('[^a-z]', '',letters))

    words = [re.sub('[^a-z]', '',letters) for letters in words]

    stopwords = load_stopwords('stopwords.txt')
    # for letters in words:
    #     if letters not in stopwords:
    #         words1.append(letters)

    words = [letters for letters in words if letters not in stopwords]

    return words

def  build_search_index(docs):
    docs = list(map(filtering,docs))

    # computers  -  [(0, 2, 4), 3]

    dictionary = dict()
    
    for line in docs:
        for word in line:
            if word not in dictionary:
                dictionary[word] = [[docs.index(line)],1]
            else:
                dictionary[word][0].append(docs.index(line))
                dictionary[word][1]+=1
    for words in dictionary:
        dictionary[words][0] = set(dictionary[words][0])

    # print(dictionary)
    return dictionary 



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
    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
