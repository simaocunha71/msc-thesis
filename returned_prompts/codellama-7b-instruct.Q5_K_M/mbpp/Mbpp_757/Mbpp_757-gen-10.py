"""
def count_reverse_pairs(words):
    return sum(1 for w1, w2 in zip(words, words[1:]) if w1[::-1] == w2)
"""
