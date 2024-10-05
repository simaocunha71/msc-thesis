    if not test:
        return {}

    letters = test.split()
    max_count = max(len(letter) for letter in letters)
    max_letter = max(set(letters), key=letters.count)

    return {max_letter: max_count}


