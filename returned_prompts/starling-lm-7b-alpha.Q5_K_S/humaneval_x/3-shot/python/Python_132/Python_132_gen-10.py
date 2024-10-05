    def is_nested(s):
        c = 0
        for c in s:
            if c == "[":
                c += 1
            elif c == "]":
                c -= 1
            if c < 0:
                return True
        return False


