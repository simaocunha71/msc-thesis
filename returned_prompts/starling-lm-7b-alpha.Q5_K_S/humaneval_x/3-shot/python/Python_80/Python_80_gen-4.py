    def is_happy(s):
        if len(s) < 3:
            return False
        return len(set(s[i:i+3] for i in range(len(s)-2))) == len(s) - 2


