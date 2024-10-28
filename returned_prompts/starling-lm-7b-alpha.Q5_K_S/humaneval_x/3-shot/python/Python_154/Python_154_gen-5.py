    def check(sub, main):
        for i in range(len(main)):
            if main.find(sub, i) != -1:
                return True
        return False

    result = False

    for i in range(len(a)):
        sub = a[i:] + a[:i]
        if check(sub, b):
            result = True
            break

    return result


