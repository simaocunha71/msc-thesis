    vowels = ['a', 'e', 'i', 'o', 'u']
    new_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                new_char = chr(ord(char) + 2)
            else:
                new_char = char.swapcase()
            new_message += new_char
        else:
            new_message += char
    return new_message

