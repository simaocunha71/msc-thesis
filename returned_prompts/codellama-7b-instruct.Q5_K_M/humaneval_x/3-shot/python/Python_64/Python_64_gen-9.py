    vowels = ["a", "e", "i", "o", "u", "y"]
    result = 0
    for c in s:
        if c.islower():
            c = c.upper()
        if c in vowels:
            result += 1
    return result


