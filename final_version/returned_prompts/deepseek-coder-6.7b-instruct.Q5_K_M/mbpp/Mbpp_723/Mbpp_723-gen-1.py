"""
def count_same_pair(l1, l2):
    return sum(1 for a, b in zip(l1, l2) if a == b)

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])) # 4
"""
