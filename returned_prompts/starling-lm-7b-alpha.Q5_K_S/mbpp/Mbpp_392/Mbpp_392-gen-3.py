
def get_max_sum(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2 or n == 3 or n == 4 or n == 5:
        return n
    else:
        return max(get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5), n)


