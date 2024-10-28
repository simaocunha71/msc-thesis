    if not test:
        return {}

    letters = test.split()
    letter_count = {}

    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    max_count = max(letter_count.values())
    max_letters = [letter for letter, count in letter_count.items() if count == max_count]

    return {letter: max_count for letter in max_letters}
#


