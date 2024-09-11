from collections import Counter
def count_reverse_pairs(strings):
    return sum(Counter(string[::-1] for string in strings).values())