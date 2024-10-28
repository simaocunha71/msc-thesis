    def check(a, b):
        for i in range(len(b)):
            if a.find(b[i:] + b[:i]) != -1:
                return True

        return False

    return check(a, b) or check(a, b[1:] + b[:1])


