def count_up_to(n):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [i for i in range(n) if is_prime(i)]

print(count_up_to(5))  # [2, 3]
print(count_up_to(11))  # [2, 3, 5, 7]
print(count_up_to(0))  # []
print(count_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))  # []
print(count_up_to(18))  # [2, 3, 5, 7, 11, 13, 17]