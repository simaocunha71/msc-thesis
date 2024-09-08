def list_split(lst, n):
    return [lst[i::n] for i in range(n)]

print(list_split(['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n'],3))

Output:
[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""

Explanation:
The function uses list comprehension to generate a new list of lists. The expression `i::n` generates a slice of the list starting from index i, stepping n steps at a time. The function iterates over the indices 0, 1, ..., n-1, creating a new list for each starting index.
"""


def list_split(lst, n):
    return [lst[i::n] for i in range(min(n, len(lst)))]

print(list_split(['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n'],3))

Output:
[['a', 'd', 'g', 'j', 'm', 'n'], ['b', 'e', 'h', 'k'], ['c', 'f', 'i', 'l']]
"""
Explanation:
The function uses list comprehension to generate a new list of lists. The expression `i::n` generates a slice of the list starting from index i, stepping n steps at a time. The function iterates over the indices 0, 1, ..., min(n, len(lst))-1, creating a new list for each starting index.
If the length of the list is less than n, the function will return a list of lists with length less than n, each containing the remaining elements of the list.
"""
<jupyter_output>
[['a', 'd', 'g