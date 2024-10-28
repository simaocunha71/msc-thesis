    vowels = ["a", "e", "i", "o", "u", "y"]
    result = 0
    for char in s:
        if char in vowels:
            result += 1
    return result


