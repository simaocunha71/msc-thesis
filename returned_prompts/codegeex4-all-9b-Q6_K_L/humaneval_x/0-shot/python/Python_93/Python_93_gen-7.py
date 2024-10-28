def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_message = ''
    for char in message:
        if char.lower() in vowels:
            new_char = chr(ord(char) + 2)
            if char.isupper():
                new_char = new_char.upper()
            new_message += new_char
        else:
            if char.isupper():
                new_message += char.lower()
            else:
                new_message += char.upper()
    return new_message

print(encode('test'))
print(encode('This is a message'))