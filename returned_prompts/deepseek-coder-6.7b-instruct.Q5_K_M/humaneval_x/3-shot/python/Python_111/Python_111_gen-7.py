    letter_counts = {}
    max_count = 0
    for letter in test.split():
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
        if letter_counts[letter] > max_count:
            max_count = letter_counts[letter]
    
    return {k: v for k, v in letter_counts.items() if v == max_count}

