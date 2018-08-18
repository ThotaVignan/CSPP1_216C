''' program for finding a element'''
def search(search_index, query):
    '''finding the doc index for search element'''
    query = query.split(' ')
    Search_result = set()
    for data in query:
        if data in search_index:
            for freq in search_index[data]:
                Search_result.add(freq[0])
        else:
            return "set()"
    return Search_result

def process_queries(search_index, queries):
    ''' processing the given queries '''
    result = [search(search_index, data) for data in queries]
    
    for output in result:
        print(output)

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

    # call process queries
    process_queries(search_index, queries)

if __name__ == '__main__':
    main()