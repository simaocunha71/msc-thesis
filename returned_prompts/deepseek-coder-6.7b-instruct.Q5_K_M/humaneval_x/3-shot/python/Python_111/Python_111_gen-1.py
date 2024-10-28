    counts = {}
    for letter in test.split():
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    max_count = max(counts.values()) if counts else 0
    return {letter: count for letter, count in counts.items() if count == max_count}


