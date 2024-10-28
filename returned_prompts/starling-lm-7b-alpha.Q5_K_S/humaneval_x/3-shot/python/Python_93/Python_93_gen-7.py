    def encode_helper(c):
        if c.isalpha():
            if c.islower():
                return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
            else:
                return chr((ord(c) - ord('A') + 1) % 26 + ord('A'))
        else:
            return c

    return ''.join(map(encode_helper, message))


