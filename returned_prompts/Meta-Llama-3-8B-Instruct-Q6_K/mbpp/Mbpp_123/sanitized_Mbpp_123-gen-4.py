def amicable_numbers_sum(n):
    def is_amicable(a, b):
        if a == b:
            return False
        if a % b != 0:
            return False
        sum_a = sum(int(i) for i in str(a))
        sum_b = sum(int(i) for i in str(b))
        return a == sum_b and b == sum_a

    sum = 0
    for i in range(1, n):
        for j in range(i, n):
            if is_amicable(i, j):
                sum += i + j
    return sum