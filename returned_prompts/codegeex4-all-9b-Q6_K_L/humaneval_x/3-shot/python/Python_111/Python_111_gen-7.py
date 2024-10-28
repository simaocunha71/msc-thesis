    from collections import Counter

    words = test.split()
    word_count = Counter(words)
    max_count = max(word_count.values())

    return {word: count for word, count in word_count.items() if count == max_count}

