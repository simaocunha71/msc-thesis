"""
def max_occurrences(lst):
    counts = {}
    for i in lst:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1
    max_count = 0
    max_item = None
    for k,v in counts.items():
        if v > max_count:
            max_count = v
            max_item = k
    return max_item

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))
"""


def max_occurrences(lst):
    counts = {}
    for i in lst:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1
    max_count = max(counts.values())
    for k,v in counts.items():
        if v == max_count:
            return k

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))


def max_occurrences(lst):
    counts = {}
    for i in lst:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1
    max_count = max(counts.values())
    for k,v in counts.items():
        if v == max_count:
            return k

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))


def max_occurrences(lst):
    counts = {}
    for i in lst:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1
    max_count = max(counts.values())
   