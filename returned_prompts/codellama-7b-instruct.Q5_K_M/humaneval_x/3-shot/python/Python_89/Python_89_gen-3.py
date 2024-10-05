    def rot(c):
        return chr(ord(c) + 2 * 2)

    return ''.join(rot(c) if c.isalpha() else c for c in s)


