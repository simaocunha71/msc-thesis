
def find_Index(n):
    t = 0
    i = 1
    while len(str(t)) < n:
        t += i
        i += 1
    return i - 1


