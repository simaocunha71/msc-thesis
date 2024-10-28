    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def rot(n, s):
        return alphabet[n % len(alphabet) + s]

    return ''.join(rot(ord(c) - ord('a'), 2) for c in s)


