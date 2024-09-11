def add_pairwise(tup):
    res = []
    for i in range(len(tup)-1):
        res.append(tup[i]+tup[i+1])
    res.append(tup[-1]+tup[-2])
    return tuple(res)


# assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
# print(add_pairwise((1, 5, 7, 8, 10)))


"""
The function takes a tuple and iterates over it in a for loop. For each iteration, it adds the current element to the next element (if it exists) and appends the result to the result list. Finally, it returns a tuple of the result list.

The function uses a for loop to iterate over the tuple. The range function is used to generate a sequence of indices from 0 to the length of the tuple minus 1. For each index i, the function adds the element at index i to the element at index i+1 (if it exists), and appends the result to the result list. If the tuple has only one element, the function will only add it to itself and append the result to the result list.

The function uses the append method to add elements to the result list. The tuple method is used to convert the result list to a tuple and return it as the final result.

The assert statement is used to check if the function returns the expected result for the given tuple (1, 5, 7, 8, 10). The expected result is (6, 12, 15, 18). The print statement is used to print the result of the function for the given tuple (1, 5, 7, 8, 10).
"""





















"""
The function takes a tuple as an argument and returns a tuple of the pairwise sums of the neighboring elements. It does this by iterating over the tuple and adding each element to the next one (if it exists), appending the result to a result list. Finally, it converts the result list to a tuple and returns