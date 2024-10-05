
from collections import Counter


def find_max(words):
    counts = Counter()
    for word in words:
        counts[word] += 1

    max_count = max(counts.values())
    max_count_words = [word for word, count in counts.items() if count == max_count]

    max_count_words.sort()
    return max_count_words[0]




def find_max(words):
    counts = {}
    for word in words:
        counts[word] = len(set(word))

    max_count = max(counts.values())
    max_count_words = [word for word, count in counts.items() if count == max_count]

    max_count_words.sort()
    return max_count_words[0]


```