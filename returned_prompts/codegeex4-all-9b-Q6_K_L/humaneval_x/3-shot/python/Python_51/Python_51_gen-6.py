    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    return ''.join([c for c in text if c.lower() not in vowels])


