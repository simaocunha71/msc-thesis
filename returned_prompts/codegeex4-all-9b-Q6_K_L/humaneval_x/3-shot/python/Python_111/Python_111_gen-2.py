    from collections import Counter

    letter_counts = Counter(test.split())
    max_count = max(letter_counts.values(), default=0)

    return {letter: count for letter, count in letter_counts.items() if count == max_count}


