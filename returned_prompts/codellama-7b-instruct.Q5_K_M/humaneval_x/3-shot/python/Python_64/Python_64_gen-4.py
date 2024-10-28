    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for c in s:
        if c in vowels or (c == "y" and s[-1] == c):
            count += 1

    return count


