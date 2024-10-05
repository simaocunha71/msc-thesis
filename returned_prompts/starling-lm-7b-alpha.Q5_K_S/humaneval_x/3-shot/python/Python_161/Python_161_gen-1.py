    def solve(s):
        if not any(c.isalpha() for c in s):
            return s[::-1]
        return ''.join(map(lambda x: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'[64 if x.isalpha() else 0::2].__getitem__(x), s))


