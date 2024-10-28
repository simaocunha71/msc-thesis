    def check(s1, s2):
        for i in range(len(s1)):
            if s1[i:] == s2:
                return True
        return False

    return check(a, b) or check(a, b[:-1]) or check(a, b[1:]) or check(a, b[-1:] + b[:-1])


