def find_star_num(n):
    def is_star_num(num):
        return all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

    count = 0
    num = 2
    while count < n:
        if is_star_num(num):
            count += 1
        num += 1
    return num - 1