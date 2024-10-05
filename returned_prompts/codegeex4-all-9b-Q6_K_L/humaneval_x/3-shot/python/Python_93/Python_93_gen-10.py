    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = ''
    
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                result += chr(ord(char) + 2)
            else:
                result += char.swapcase()
        else:
            result += char
    
    return result

