
    def solve(s):
        i = 0
        while i < len(s):
            if s[i].isalpha():
                if s[i].islower():
                    s = s[:i] + s[i].upper() + s[i+1:]
                else:
                    s = s[:i] + s[i].lower() + s[i+1:]
            i += 1
        return s
