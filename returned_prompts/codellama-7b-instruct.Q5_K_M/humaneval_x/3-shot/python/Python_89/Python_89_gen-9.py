    def encrypt(s):
        res = ""
        for c in s:
            if c.isalpha():
                if c.isupper():
                    res += chr((ord(c) - ord('A') + 2) % 26 + ord('A'))
                else:
                    res += chr((ord(c) - ord('a') + 2) % 26 + ord('a'))
            else:
                res += c
        return res


