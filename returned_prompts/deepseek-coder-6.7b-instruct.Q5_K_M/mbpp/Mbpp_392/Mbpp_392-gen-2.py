
def get_max_sum(n):
    if n <= 1:
        return n
    return max(get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5), n)


