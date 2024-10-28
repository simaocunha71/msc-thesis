
def by_length(arr):
    # list of English words corresponding to numbers 1-9
    num_to_word = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    # filter out numbers not in the range 1-9, then sort, reverse and map to words
    return list(map(lambda x: num_to_word[x-1], sorted(filter(lambda x: 1 <= x <= 9, arr), reverse=True)))

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([]))  # []
print(by_length([1, -1, 55]))  # ['One']

The function by_length sorts the input array and filters out any numbers that are not 1-9. It then reverses the sorted array and maps each number to its corresponding English word.
"""

"""
E:

def by_length(arr):
    return [["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"][i-1] for i in sorted([i for i in arr if 1 <= i <= 9], reverse=True)]

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([]))  # []
print(by_length([1, -1, 55]))  # ['One']
"""

"""
S:

def by_length(arr):
    return [["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"][i-1] for i in sorted([i for i in arr if 1 <= i <= 9], reverse=True)]

print(by_length([2, 1, 