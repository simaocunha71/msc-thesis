    def encrypt(s):
        result = ''
        for c in s:
            if c.isalpha():
                n = ord(c)
                if c.islower():
                    n += 2
                    if n > ord('z'):
                        n -= 26
                else:
                    n += 2
                    if n > ord('Z'):
                        n -= 26
                result += chr(n)
            else:
                result += c
        return result


