    letter_counts = {}
    for letter in test.split():
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1

    max_count = max(letter_counts.values())
    return {k: v for k, v in letter_counts.items() if v == max_count}


