    vowels = "aeiou"
    count = 0
    for idx, elem in enumerate(s):
        if elem.isupper() and elem in vowels and idx % 2 == 0:
            count += 1
    return count


