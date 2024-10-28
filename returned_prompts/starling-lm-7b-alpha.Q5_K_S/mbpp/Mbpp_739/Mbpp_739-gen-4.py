
def find_Index(n: int) -> int:
    for i in range(1, n+1):
        if len(str(i*(i+1)//2)) == n:
            return i*(i+1)//2


