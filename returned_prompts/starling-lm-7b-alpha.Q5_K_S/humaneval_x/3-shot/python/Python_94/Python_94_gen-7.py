    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def digit_sum(n: int) -> int:
        result = 0
        while n > 0:
            result += n % 10
            n //= 10
        return result

    result = 0
    for l in lst:
        if is_prime(l):
            result += digit_sum(l)

    return result


