
def combinations_list(lst):
    res = [[]]
    for i in range(len(lst)):
        res += [x + [lst[i]] for x in res]
    return res

print(combinations_list(['orange',  'red',  'green',  'blue']))

"""
The function first initializes the result list with an empty list []. Then it goes through every element in the given list. For each element, it creates a new list by adding the current element to each possible list from the result list. It then adds these new lists to the result list. The process is repeated until all elements in the given list have been processed. Finally, the result list is returned.
"""

"""
