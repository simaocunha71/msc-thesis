    if len(b) > len(a):
        return False
    else:
        for i in range(len(a) - len(b) + 1):
            if a[i:i+len(b)] == b or a[i:i+len(b)] == b[::-1]:
                return True
        return False


