    count = 0
    vowels = "aeiou"

    for letter in s:
        if letter.lower() in vowels:
            count += 1

    if s[-1] == 'y':
        count += 1

    return count


