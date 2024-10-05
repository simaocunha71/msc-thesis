    result = ''

    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
                    result += chr(ord(letter) + 2 * 2)
                else:
                    result += letter
            else:
                if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
                    result += chr(ord(letter) + 2 * 2)
                else:
                    result += letter
        else:
            result += letter

    return result


