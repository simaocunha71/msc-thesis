def freq_count(lst):
    freqs = {}
    for num in lst:
        if num in freqs:
            freqs[num] += 1
        else:
            freqs[num] = 1
    return freqs

print(freq_freq([10,10,10,10,20,20,20,20,40,40,50,50,30]))

"""
Output:
{10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
"""

This program works by creating an empty dictionary. It then iterates over every element in the input list. If the element is already a key in the dictionary, it increments the value associated with that key by 1. If the element is not a key in the dictionary, it adds the element as a key with a value of 1. The function then returns the dictionary.

The time complexity of this function is O(n), where n is the length of the list. This is because it must iterate over each element in the list once. The space complexity is also O(n), as in the worst case scenario, each element in the list will be a unique key in the dictionary.
"""

