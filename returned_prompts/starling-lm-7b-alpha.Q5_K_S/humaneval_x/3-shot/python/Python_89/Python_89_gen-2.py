    def encrypt(s):
        result = ""
        for c in s:
            if c.isalpha():
                if c.islower():
                    result += chr((ord(c) - ord('a') + 2 * 2 + 26) % 26 + ord('a'))
                else:
                    result += chr((ord(c) - ord('A') + 2 * 2 + 26) % 26 + ord('A'))
            else:
                result += c
        return result


