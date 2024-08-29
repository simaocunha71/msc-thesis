def max_occurrences(lst):
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    max_freq = max(count.values())
    for key, value in count.items():
        if value == max_freq:
            return key

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))

# Solution 2:
def max_occurrences(lst):
    return max(set(lst), key=lst.count)

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))

# Solution 3:
from collections import Counter

def max_occurrences(lst):
    c = Counter(lst)
    return c.most_common(1)[0][0]

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))
<jupyter_output>
2
2
2
<jupyter_text>
Question 2: Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.
<jupyter_code>
