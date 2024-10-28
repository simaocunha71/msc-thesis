def find_star_num(n):
    def count_prime_factors(num):
        count = 0
        while num % 2 == 0:
            count += 1
            num = num // 2
        for i in range(3, int(num**0.5) + 1, 2):
            while num % i == 0:
                count += 1
                num = num // i
        if num > 2:
            count += 1
        return count

    star_num = 0
    i = 2
    while True:
        if count_prime_factors(i) == 1:
            star_num += 1
        if star_num == n:
            return i
        i += 1