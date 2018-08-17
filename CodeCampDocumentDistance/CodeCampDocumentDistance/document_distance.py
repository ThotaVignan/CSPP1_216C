import collections,math,re
'''
    Document Distance - A detailed description is given in the PDF
'''
def similarity_calucalation(num,den1,den2):
    result = num/(den1*den2)
    return result
def denaminator_product(data):
    # print(data,"data")
    sum_of_pow_freq = 0
    for freq in data:
        sum_of_pow_freq += data[freq]**2
    print(sum_of_pow_freq,"sum")
    return math.sqrt(sum_of_pow_freq)


def numerator_product(data1,data2):
    product = 0
    for word in data1:
        if word in data2:
            product+=data1[word]*data2[word]
    return product


def remove_stopwords(data):
    stopword = load_stopwords("stopwords.txt")
    data1 = data.copy()
    for word in data1:
        if word in stopword:
            del data[word]
    return data

def format_data(data):
    lower=data.lower()
    case = re.sub('[^a-z\ ]', '', lower)
    return case

def freq_count(b):
   
    s=b.split(' ')
    count=collections.Counter(s)
    
    return count
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1 = format_data(dict1)
    dict2 = format_data(dict2)
    freq1 = freq_count(dict1)
    freq2 = freq_count(dict2)
    swords1 = remove_stopwords(freq1)
    swords2 = remove_stopwords(freq2)
    numerator =  numerator_product(swords1,swords2)
    denaminator1 = denaminator_product(swords1)
    denaminator2 = denaminator_product(swords2)
    # print(denaminator1,denaminator2)
    matching_similarity = similarity_calucalation(numerator,denaminator1,denaminator2)
    return matching_similarity


def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
