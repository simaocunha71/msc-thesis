    if a.find(b) != -1:
        return True
    else:
        for i in range(len(b)):
            if a.find(b[i:] + b[:i]) != -1:
                return True
        return False


