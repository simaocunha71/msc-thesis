def Find_Max(lst):
    max_len = max(len(sublist) for sublist in lst)
    for sublist in lst:
        if len(sublist) == max_len:
            return sublist

print(Find_Max([['A'],['A','B'],['A','B','C']]))

# Output: ['A', 'B', 'C']

Explanation:
This program works by first finding the length of the longest list in the given list of lists (`max_len`). It then iterates over the given list of lists, and returns the first list it finds whose length matches `max_len`.

In the case of the given example, the function returns the list ['A', 'B', 'C'] because it is the longest list in the list of lists.
"""

# 