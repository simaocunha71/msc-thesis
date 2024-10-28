    def rotate(c):
        if c.isalpha():
            return chr((ord(c) + 2 * 2 - ord('a')) % 26 + ord('a'))
        else:
            return c

    return "".join(rotate(c) for c in s)

