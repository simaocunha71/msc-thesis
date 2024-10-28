"""
def find_even_pair(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] ^ lst[j] % 2 == 0:
                pairs += 1
    return pairs
"""
