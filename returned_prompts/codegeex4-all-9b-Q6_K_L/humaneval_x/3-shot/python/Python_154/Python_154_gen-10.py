    def check_rotation(b, a):
        for i in range(len(a)):
            if a[i:] + a[:i] == b:
                return True
        return False

    return check_rotation(b, a) or check_rotation(b[::-1], a) or check_rotation(b[::-1], a[::-1])

