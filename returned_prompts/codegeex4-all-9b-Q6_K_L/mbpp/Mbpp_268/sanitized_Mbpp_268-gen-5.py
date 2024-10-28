def find_star_num(n):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    def star_number(num):
        return sum(find_factors(num))

    count = 0
    i = 1
    while count < n:
        if star_number(i) == i:
            count += 1
        i += 1

    return i - 1