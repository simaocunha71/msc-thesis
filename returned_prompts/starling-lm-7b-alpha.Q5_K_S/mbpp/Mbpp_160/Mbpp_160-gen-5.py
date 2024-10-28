
def find_solution(a:int,b:int,n:int) -> tuple:
    x = n
    y = 0
    while x % a != 0:
        x -= b * (x % a)
        y += 1
    if x % a == 0:
        return (x//a, y)
    else:
        return None


