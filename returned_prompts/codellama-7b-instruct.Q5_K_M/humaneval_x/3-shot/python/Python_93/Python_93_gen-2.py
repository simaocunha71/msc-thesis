    def encode_char(char):
        if char.isalpha():
            if char.islower():
                return chr((ord(char) + 2) % 26 + ord('a'))
            else:
                return chr((ord(char) - 2) % 26 + ord('A'))
        else:
            return char

    return ''.join(encode_char(char) for char in message)

