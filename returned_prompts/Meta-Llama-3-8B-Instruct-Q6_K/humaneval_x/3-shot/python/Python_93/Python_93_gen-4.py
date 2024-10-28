    vowels = 'aeiouAEIOU'
    result = ''

    for char in message:
        if char in vowels:
            if char.islower():
                result += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
        else:
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()

    return result


