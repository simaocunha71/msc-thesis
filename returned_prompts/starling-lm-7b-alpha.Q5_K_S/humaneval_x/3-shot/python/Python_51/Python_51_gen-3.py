    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    result = ''.join(c for c in text if c.lower() not in vowels)
    return result


