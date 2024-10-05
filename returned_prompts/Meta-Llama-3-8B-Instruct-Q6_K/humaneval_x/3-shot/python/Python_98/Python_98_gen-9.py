    count = 0
    for i in range(0, len(s), 2):
        char = s[i]
        if char in 'AEIOU' and char.isupper():
            count += 1
    return count


