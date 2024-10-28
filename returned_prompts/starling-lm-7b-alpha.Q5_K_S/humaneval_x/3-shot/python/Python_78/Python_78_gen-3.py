    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def hex_key(num):
        result = 0
        for digit in num:
            if is_prime(int(digit, 16)):
                result += 1
        return result


