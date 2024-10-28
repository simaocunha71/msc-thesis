    def get_new_char(char, offset):
        if char.isalpha():
            return chr((ord(char) + offset - ord('a') - 1) % 26 + ord('a'))
        else:
            return char

    offset = ord('a') - ord('A')
    return ''.join(get_new_char(char, offset) for char in message)


