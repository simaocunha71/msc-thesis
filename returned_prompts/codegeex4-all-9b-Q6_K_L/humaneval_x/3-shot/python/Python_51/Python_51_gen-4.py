    vowels = ['a', 'e', 'i', 'o', 'u']
    new_text = ''

    for c in text:
        if c.lower() not in vowels:
            new_text += c

    return new_text

