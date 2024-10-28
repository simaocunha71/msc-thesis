
def sum_of_divisors(n1: int,n2: int) -> int:
    def sum_divisors(n: int) -> int:
        result = 1
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor:
                divisor += 1
            else:
                n //= divisor
                result *= divisor + n
                divisor = 1
        if divisor > 1:
            result *= n + divisor
        return result
    return sum_divisors(n1) + sum_divisors(n2)


