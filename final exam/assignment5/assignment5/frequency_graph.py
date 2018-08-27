'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

# def frequency_graph(dictionary):
#     pass

# def main():
#     dictionary = eval(input())
#     frequency_graph(dictionary)

# if __name__ == '__main__':
#     main()

'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''dictionary'''
    dic = dictionary
    keys = sorted(dictionary)
    for key in keys:
        count  = dictionary[key]
        value  = ''
        for i in range(0, count, 1):
            value += '#'

        # print(value)  
        print(key+' '+'-'+' '+value)

def main():
    '''main'''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()