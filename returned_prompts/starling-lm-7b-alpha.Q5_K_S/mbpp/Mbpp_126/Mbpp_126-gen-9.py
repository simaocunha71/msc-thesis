
def sum_common_divisors(num1, num2):
    result = 0
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            result += i
    return result


