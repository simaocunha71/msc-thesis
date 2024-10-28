    vowels = 'aeiouAEIOU'
    message = message.swapcase()
    result = ''
    for char in message:
        if char in vowels:
            if char.islower():
                result += chr(ord(char) + 2)
            else:
                result += chr(ord(char) + 2)
        else:
            result += char
    return result


