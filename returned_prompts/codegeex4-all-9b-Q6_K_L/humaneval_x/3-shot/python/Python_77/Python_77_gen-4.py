    def iscube(a):
        if a == 0:
            return True
        for i in range(-100000, 100000):
            if i ** 3 == a:
                return True
        return False

    return iscube(a)

