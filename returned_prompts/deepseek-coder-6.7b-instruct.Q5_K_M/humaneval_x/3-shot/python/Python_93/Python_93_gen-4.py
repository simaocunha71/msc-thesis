    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char in vowels:
            if char.islower():
                result += chr((ord(char) - 97 + 2) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + 2) % 26 + 65)
        else:
            result += char.swapcase()
    return result


