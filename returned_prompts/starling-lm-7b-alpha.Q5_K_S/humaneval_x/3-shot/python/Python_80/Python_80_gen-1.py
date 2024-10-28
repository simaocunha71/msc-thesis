    def is_happy(s):
        if len(s) < 3:
            return False
        return len(set(s[i:i+3] for i in range(0, len(s), 3))) == len(s[i:i+3] for i in range(0, len(s), 3))


