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
    print(x_or_y(7, 34, 12))  # Output: 34
    print(x_or_y(15, 8, 5))   # Output: 5
    print(x_or_y(3, 34, 12))  # Output: 34
    print(x_or_y(4, 8, 5))    # Output: 5
    print(x_or_y(5, 34, 12))  # Output: 34
    print(x_or_y(6, 8, 5))    # Output: 5
    print(x_or_y(8, 34, 12))  # Output: 5
    print(x_or_y(9, 8, 5))    # Output: 5
    print(x_or_y(10, 34, 12)) # Output: 5
    print(x_or_y(11, 34, 12)) # Output: 34
    print(x_or_y(12, 8, 5))   # Output: 5
    print(x_or_y(13, 34, 12)) # Output: 34
    print(x_or_y(14, 8, 5))   # Output: 5
    print(x_or_y(16, 34, 12)) # Output: 5
    print(x_or_y(17, 34, 12)) # Output: 34
    print(x_or_y(18, 8, 5))   # Output: 5
    print(x_or_y(19, 34, 12)) # Output: 34
    print(x_or_y(20, 8, 5))   # Output: 5
    print(x_or_y(21, 34, 12)) # Output: 5
    print(x_or_y(22, 8, 5))   # Output: 5
    print(x_or_y(23, 34, 12)) # Output: 