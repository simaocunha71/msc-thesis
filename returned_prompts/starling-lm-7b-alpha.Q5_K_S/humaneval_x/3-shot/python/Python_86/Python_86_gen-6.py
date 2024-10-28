    def anti_shuffle(s):
        chars = []
        for c in s:
            if c != ' ':
                chars.append(chr(ord(c) - 1))
            else:
                chars.append(c)

        return ''.join(chars)


