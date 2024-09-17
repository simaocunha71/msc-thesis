def is_polite(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, n+1):
        if n % i == 0:
            return False
    return True

def polite_number(n: int) -> int:
    count = 0
    num = 1
    while count < n:
        if is_polite(num):
            count += 1
        num += 1
    return num - 1

