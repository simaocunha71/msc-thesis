"""
def count_reverse_pairs(lst):
    counter = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i][::-1] == lst[j][::-1]:
                counter += 1
    return counter
"""
