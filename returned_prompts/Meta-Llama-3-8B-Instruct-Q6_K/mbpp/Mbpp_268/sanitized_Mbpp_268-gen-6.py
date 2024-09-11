def find_star_num(n):
    star_nums = []
    k = 1
    while len(star_nums) < n:
        if is_prime(k):
            star_nums.append(k)
        k += 1
    return star_nums[-1]
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True