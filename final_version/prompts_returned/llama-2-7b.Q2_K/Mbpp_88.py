"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""
import collections
def freq_count(lst):
    freq = collections.Counter()   # Counter is a built-in type with the same methods as maps in python3
    for num in lst:
        freq[num] += 1                           # Adds one to the count of that value if it does not already exist, otherwise sets that count to one less than its current value.
    return freq
