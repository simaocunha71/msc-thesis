    letter_count = {}
    max_count = 0

    for letter in test:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

        if letter_count[letter] > max_count:
            max_count = letter_count[letter]

    result = {}
    for letter, count in letter_count.items():
        if count == max_count:
            result[letter] = count

    return result

