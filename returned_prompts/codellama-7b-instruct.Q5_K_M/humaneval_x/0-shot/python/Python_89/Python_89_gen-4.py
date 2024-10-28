
def encrypt(s):
    def shift(c):
        return chr((ord(c) - ord('a') + 2 * 2) % 26 + ord('a'))
    return ''.join(shift(c) for c in s)


