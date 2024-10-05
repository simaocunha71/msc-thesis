    a = list(a)
    b = list(b)
    for i in range(len(b)):
        a.append(b[i])
        if ''.join(a) in ''.join(a):
            return True
        else:
            return False


