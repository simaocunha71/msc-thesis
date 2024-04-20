"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""
from collections import Counter
def longest_word(word_list):
    def _count_words(word, result):
        if word not in counter:
            counter[word] = 0
        counter[word] += 1
    counter = Counter()
    for word in word_list:
        _count_words(word, counter)

    return max(counter.items(), key=lambda x: (x[1], -x[0]))[0][0]