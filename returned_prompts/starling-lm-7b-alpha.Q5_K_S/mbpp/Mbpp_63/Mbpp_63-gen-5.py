"""
def max_difference(list_tup):
    max_diff = 0
    for i in range(len(list_tup)):
        for j in range(i + 1, len(list_tup)):
            diff = max(list_tup[i][0], list_tup[i][1]) - min(list_tup[j][0], list_tup[j][1])
            if diff > max_diff:
                max_diff = diff
    return max_diff

print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)])) #7
"""

def max_difference(list_tup):
    max_diff = 0
    for i in range(len(list_tup)):
        for j in range(i + 1, len(list_tup)):
            diff = max(list_tup[i][0], list_tup[i][1]) - min(list_tup[j][0], list_tup[j][1])
            if diff > max_diff:
                max_diff = diff
    return max_diff

print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)])) #7












"""

def max_difference(list_tup):
    max_diff = 0
    for i in range(len(list_tup)):
        for j in range(i + 1, len(list_tup)):
            diff = max(list_tup[i][0], list_tup[i][1]) - min(list_tup[j][0], list_tup[j][1])
            if diff > max_diff:
                max_diff = diff
    return max_diff

print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)])) #7
"""
def max_difference(list_tup):
    max_diff