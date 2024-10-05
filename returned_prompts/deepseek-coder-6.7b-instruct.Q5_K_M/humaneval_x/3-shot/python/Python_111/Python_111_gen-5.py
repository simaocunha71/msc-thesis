    letter_count = {}

    for letter in test.split():
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1

    max_count = max(letter_count.values()) if letter_count else 0

    return {k: v for k, v in letter_count.items() if v == max_count}


