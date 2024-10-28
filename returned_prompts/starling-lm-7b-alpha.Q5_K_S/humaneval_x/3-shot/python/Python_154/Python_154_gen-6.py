    def check(b):
        for i in range(len(b)):
            if a.find(b[i:]) != -1:
                return True
        return False

    return check(b) or check(b[1:] + b[0]) or check(b[2:] + b[1:] + b[0])


