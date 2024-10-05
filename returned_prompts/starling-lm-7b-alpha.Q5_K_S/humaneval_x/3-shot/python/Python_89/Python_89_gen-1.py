    def encrypt(s):
        result = ""
        for c in s:
            if c.isalpha():
                # shift letters down by two multiplied to two places
                result += chr(ord(c) + 2*2)
            else:
                result += c
        return result


