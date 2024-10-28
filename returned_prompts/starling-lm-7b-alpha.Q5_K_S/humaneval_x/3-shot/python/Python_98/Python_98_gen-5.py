    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for i, char in enumerate(s):
        if char in vowels and i % 2 == 0:
            count += 1
    return count


