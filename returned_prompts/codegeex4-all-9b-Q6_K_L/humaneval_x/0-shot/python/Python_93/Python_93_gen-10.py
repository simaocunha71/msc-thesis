def encode(message):
    vowels = "aeiou"
    encoded = ""
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded += chr(ord(char) + 2)
            else:
                encoded += char.swapcase()
        else:
            encoded += char
    return encoded

print(encode('test'))
print(encode('This is a message'))