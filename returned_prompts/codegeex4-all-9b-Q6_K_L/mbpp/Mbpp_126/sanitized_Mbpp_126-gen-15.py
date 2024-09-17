def sum(num1: int, num2: int):
    common_divisors = set()
    for i in range(1, min(num1, num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.add(i)
    return sum(common_divisors)