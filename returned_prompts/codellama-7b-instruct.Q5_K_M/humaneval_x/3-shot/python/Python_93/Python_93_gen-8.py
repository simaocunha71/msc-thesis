    new_message = ''
    vowels = 'aeiou'
    for i, char in enumerate(message):
        if char.isalpha():
            if char.islower():
                if char in vowels:
                    new_message += vowels[vowels.index(char)+2]
                else:
                    new_message += char.upper()
            elif char.isupper():
                if char in vowels:
                    new_message += vowels[vowels.index(char)-2]
                else:
                    new_message += char.lower()
        else:
            new_message += char
    return new_message


