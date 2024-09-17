
def amicable_numbers_sum(num):
    def amicable(n):
        s = 0
        for i in range(1, n):
            if n % i == 0:
                s += i
        return sum(list(filter(lambda x: sum(list(filter(lambda y: n % y == 0, range(1, x)))) == x, range(1, s))))
    return sum(list(filter(lambda x: x <= num, amicable(x) for x in range(1, num + 1))))


