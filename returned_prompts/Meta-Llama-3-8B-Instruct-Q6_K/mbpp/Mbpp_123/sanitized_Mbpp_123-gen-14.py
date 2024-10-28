def amicable_numbers_sum(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_of_divisors(num):
        total = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
        return total

    def is_amicable(num1, num2):
        if num1 == num2:
            return False
        return sum_of_divisors(num1) == num2 and sum_of_divisors(num2) == num1

    total_sum = 0
    for i in range(2, n + 1):
        if not is_prime(i):
            for j in range(i * 2, n + 1):
                if is_amicable(i, j):
                    total_sum += i + j
    return total_sum