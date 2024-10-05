    def x_or_y(n, x, y):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        if is_prime(n):
            return x
        else:
            return y
    # Example usage:
    print(x_or_y(7, 34, 12))  # Output: 34
    print(x_or_y(15, 8, 5))   # Output: 5
    print(x_or_y(3, 9, 6))    # Output: 9
    print(x_or_y(4, 10, 7))   # Output: 7
    print(x_or_y(2, 11, 8))   # Output: 11
    print(x_or_y(1, 13, 14))  # Output: 14
    print(x_or_y(0, 15, 16))  # Output: 16
    print(x_or_y(6, 17, 18))  # Output: 18
    print(x_or_y(9, 19, 20))  # Output: 20
    print(x_or_y(11, 21, 22)) # Output: 21
    print(x_or_y(12, 23, 24)) # Output: 24
    print(x_or_y(13, 25, 26)) # Output: 25
    print(x_or_y(14, 27, 28)) # Output: 28
    print(x_or_y(15, 29, 30)) # Output: 30
    print(x_or_y(16, 31, 32)) # Output: 31
    print(x_or_y(17, 33, 34)) # Output: 33
    print(x_or_y(18, 35, 36)) # Output: 36
    print(x_or_y(19, 37, 38)) # Output: 37
    print(x_or_y(20, 39, 40)) # Output: 40
    print(x_or_y(21, 41, 42)) # Output: 41
    print(x_or_y(22, 43, 44)) # Output: