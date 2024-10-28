    vowels = ["a", "e", "i", "o", "u"]
    result = 0
    for i, c in enumerate(s):
        if c in vowels and i % 2 == 0:
            result += 1
    return result


