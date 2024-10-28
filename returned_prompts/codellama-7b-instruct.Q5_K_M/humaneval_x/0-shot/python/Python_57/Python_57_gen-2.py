
def monotonic(l: list):
    if len(l) < 2:
        return True
    if l[1] - l[0] < 0:
        return False
    for i in range(2, len(l)):
        if l[i] - l[i-1] < 0:
            return False
    return True
