def get_ludic(n: int) -> list:
    ludic = [1]
    for i in range(2, n+1):
        if is_ludic(i):
            ludic.append(i)
    return ludic

def is_ludic(n: int) -> bool:
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            if n % (n-i) == 0:
                return False
    return True

