
def find_Index(n):
    for i in range(1, n+1):
        num = i*(i+1)//2
        if len(str(num)) == n:
            return i
    return -1


