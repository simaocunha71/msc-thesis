    def encrypt(s):
        return ''.join(chr((ord(c) + 2 * 2) % 256) for c in s)


