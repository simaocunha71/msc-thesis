
def sum_common_divisors(num1: int, num2: int) -> int:
    divisors = set()
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors.add(i)
    return sum(divisors)


