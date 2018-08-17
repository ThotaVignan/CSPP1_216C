''' Programm to find the similarity of content between two files'''
import collections
import math
import re
def similarity_calucalation(num, den1, den2):
    ''' calculating the percentage of similarity'''
    result = num/(den1*den2)
    return result
def denaminator_product(data):
    ''' adding the frequencies of eac word in a given file'''
    sum_of_pow_freq = 0
    for freq in data:
        sum_of_pow_freq += data[freq]**2
    return math.sqrt(sum_of_pow_freq)

def numerator_product(data1, data2):
    '''Finding the product of common words in both files'''
    product = 0
    for word in data1:
        if word in data2:
            product += data1[word] * data2[word]
    return product

def remove_stopwords(data):
    '''Removing the stopwords from the given data'''
    stopword = load_stopwords("stopwords.txt")
    data1 = data.copy()
    for word in data1:
        if word in stopword:
            del data[word]
    return data

def format_data(data):
    ''' Converting the data into lowercase and removing the special characters'''
    lower = data.lower()
    regex = re.compile('[^a-z]')
    case = regex.sub('', lower)
    return case

def freq_count(data):
    '''Finding the frequency of each word in a file'''
    data1 = data.split(' ')
    data1 = [w for w in data1 if(len(w.strip())) > 0]
    count = collections.Counter(data1)
    return count

def similarity(dict1, dict2):
    '''Compute the document distance as given in the PDF'''
    dict1 = format_data(dict1)
    dict2 = format_data(dict2)
    freq1 = freq_count(dict1)
    freq2 = freq_count(dict2)
    swords1 = remove_stopwords(freq1)
    swords2 = remove_stopwords(freq2)
    numerator = numerator_product(swords1, swords2)
    denaminator1 = denaminator_product(swords1)
    denaminator2 = denaminator_product(swords2)
    matching_similarity = similarity_calucalation(numerator, denaminator1, denaminator2)
    return matching_similarity

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
