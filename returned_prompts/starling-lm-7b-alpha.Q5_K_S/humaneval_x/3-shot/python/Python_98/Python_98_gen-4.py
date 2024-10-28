    vowels = "aeiou"
    count = 0
    for idx, char in enumerate(s):
        if idx % 2 == 0 and char.lower() in vowels and char.isupper():
            count += 1
    return count


