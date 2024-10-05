    def encode_letter(letter):
        if letter.isalpha():
            if letter.islower():
                index = ord(letter) - ord('a')
                return chr(index + 1)
            else:
                index = ord(letter) - ord('A')
                return chr(index + 1)
        else:
            return letter

    result = ''.join(map(encode_letter, message))
    return result


