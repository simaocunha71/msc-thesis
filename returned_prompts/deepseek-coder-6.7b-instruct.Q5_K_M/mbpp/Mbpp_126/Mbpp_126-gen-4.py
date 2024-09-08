def sum_of_common_divisors(num1, num2):
    def get_divisors(num):
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors

    num1_divisors = get_divisors(num1)
    num2_divisors = get_divisors(num2)

    common_divisors = [num for num in num1_divisors if num in num2_divisors]
    return sum(common_divisors)


print(sum_of_common_divisors(10, 15))  # Expected output: 6


def sum_of_common_divisors(num1, num2):
    def get_divisors(num):
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors

    num1_divisors = get_divisors(num1)
    num2_divisors = get_divisors(num2)

    common_divisors = [num for num in num1_divisors if num in num2_divisors]
    return sum(common_divisors)


print(sum_of_common_divisors(10, 15))  # Expected output: 6


# Alternate solution using built-in functions
def sum_of_common_divisors(num1, num2):
    def get_divisors(num):
        return set(i for i in range(1, num + 1) if num % i == 0)

    num1_divisors = get_divisors(num1)
    num2_divisors = get_divisors(num2)

    return sum(num1_divisors & num2_divisors)


print(sum_of_common_divisors(10, 15))  # Expected output: 6


# Alternate solution using