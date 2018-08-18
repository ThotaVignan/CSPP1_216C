# ''' program for finding a element'''
# def search(search_index, query):
#     '''finding the doc index for search element'''
#     query = query.split(' ')
#     search_result = set()
#     for data in query:
#         if data in search_index:
#             for freq in search_index[data]:
#                 search_result.add(freq[0])
#         else:
#             return "set()"
#     return search_result

# def process_queries(search_index, queries):
#     ''' processing the given queries '''
#     result = [search(search_index, data) for data in queries]

#     for output in result:
#         print(output)

# def main():
#     '''
#         main function
#     '''
#     # This line loads the search index
#     search_index = eval(input())

#     # read the number of search queries
#     lines = int(input())

#     # read the search queries into a list
#     queries = []
#     for _ in range(lines):
#         queries.append(input())

#     # call process queries
#     process_queries(search_index, queries)

# if __name__ == '__main__':
#     main()
def search(search_index, query):
    '''
        function to search through the search index and return the results
        split the query into lowercase words
        check if the word is in the search_index
        collect all the values for the words that are in the search_index
        make a set of doc_id and return
    '''
    doc_id = set()
    query = query.lower().split(" ")
    # regex = re.compile('[^a-z]')
    # query = regex.sub('', query.strip())
    # print(query)
    for word in query:
        if word in search_index:
            for iterate_ in range(len(search_index[word])):

                doc_id.add(search_index[word][iterate_][0])

    return doc_id
    # pass

def process_queries(search_index, queries):
    '''
        function to process the search queries
        iterate through all the queries and call the search function
        print the results returned by search function
    '''
    # print(queries)
    for words in queries:
        print(search(search_index, words))
    # pass

def main():
    '''
        main function
    '''
    # This line loads the search index
    search_index = eval(input())

    # read the number of search queries
    lines = int(input())
    # read the search queries into a list
    queries = []
    for i in range(lines):
        queries.append(input())
        i += 1

    # call process queries
    process_queries(search_index, queries)

if __name__ == '__main__':
    main()