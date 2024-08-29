def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2 ** (n - 1).bit_length()

print(next_power_of_2(0))

# Alternate Solution
def next_power_of_2(n):
    i = 0
    while 2 ** i < n:
        i += 1
    return 2 ** i

print(next_power_of_2(0))

# Both will give same output
# 1

# Time Complexity of both solutions is O(logn)
# Space Complexity is O(1)
<jupyter_output>
1
1
<jupyter_text>
Problem 3:Write a Python function that takes a string and returns a dictionary where the keys are the words in the string and the values are the counts of each word.
<jupyter_code>
def word_count(s):
    words = s.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_count("hello world hello"))
<jupyter_output>
{'hello': 2, 'world': 1, 'hello': 2}
<jupyter_text>
Problem 4:Write a Python function that takes a list of strings and returns a list of the strings sorted by the last character of each string.
<jupyter_code>
def sort_by_last_char(lst):
    return sorted(lst, key=lambda s: s[-1])

print(sort_by_last_char(['abc', 'def', 'ghi', 'jkl']))
<jupyter_output>
['abc', 'jkl', 'ghi', 'def']
<jupyter_text>
Problem 5:Write a Python function that takes a list of integers and returns a list of the integers sorted by the sum of their digits. If two integers have the same sum of digits, they should be sorted by their