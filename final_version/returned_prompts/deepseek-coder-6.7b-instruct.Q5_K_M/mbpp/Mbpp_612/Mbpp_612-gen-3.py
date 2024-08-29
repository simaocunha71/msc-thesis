def merge(lst):
    return [[sub[i] for sub in lst] for i in range(2)]

print(merge([['x',  'y'], ['a', 'b'], ['m', 'n']]))

Explanation:
The function uses list comprehension to create new lists. For each index 'i' in the range of 2, it creates a new list that includes the 'i'th element from each sublist in the original list 'lst'.

"""
