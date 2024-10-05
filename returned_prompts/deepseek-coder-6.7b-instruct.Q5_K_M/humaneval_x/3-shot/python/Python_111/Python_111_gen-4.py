    letter_counts = {}
    max_count = 0
    for letter in test.split():
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
        max_count = max(max_count, letter_counts[letter])
    return {k: v for k, v in letter_counts.items() if v == max_count}


