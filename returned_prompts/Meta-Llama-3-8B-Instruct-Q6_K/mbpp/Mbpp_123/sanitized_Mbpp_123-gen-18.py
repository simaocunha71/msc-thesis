def amicable_numbers_sum(n):
    def is_amicable(a, b):
        if a == b:
            return False
        sum_a = sum(i for i in range(1, a) if a % i == 0)
        sum_b = sum(i for i in range(1, b) if b % i == 0)
        return sum_a == b and sum_b == a

    sum = 0
    for i in range(1, n):
        for j in range(i, n):
            if is_amicable(i, j):
                sum += i
    return sum