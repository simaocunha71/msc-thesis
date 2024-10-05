    vowels = 'aeiou'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                new_message += chr((ord(char) + 2) % 26 + ord('a')) if char.islower() else chr((ord(char) + 2) % 26 + ord('A'))
            else:
                new_message += char.swapcase()
        else:
            new_message += char
    return new_message


