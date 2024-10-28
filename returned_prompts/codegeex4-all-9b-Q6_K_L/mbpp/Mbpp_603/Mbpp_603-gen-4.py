def get_ludic(n: int) -> list:
    ludic_nums = []
    for i in range(1, n+1):
        if is_ludic(i):
            ludic_nums.append(i)
    return ludic_nums

def is_ludic(n: int) -> bool:
    return all(is_prime(i) for i in range(2, int(math.sqrt(n))+1) if n % i == 0)

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print(get_ludic(10))