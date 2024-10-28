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

    # Testing the function
    print(x_or_y(7, 34, 12))  # Should print 34
    print(x_or_y(15, 8, 5))   # Should print 5
    print(x_or_y(23, 34, 12)) # Should print 34
    print(x_or_y(20, 8, 5))   # Should print 5
    print(x_or_y(5, 34, 12))  # Should print 34
    print(x_or_y(3, 34, 12))  # Should print 34
    print(x_or_y(4, 34, 12))  # Should print 5

B:

    def x_or_y(n, x, y):
        if n <= 1:
            return y
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return y
        return x

    # Testing the function
    print(x_or_y(7, 34, 12))  # Should print 34
    print(x_or_y(15, 8, 5))   # Should print 5
    print(x_or_y(23, 34, 12)) # Should print 34
    print(x_or_y(20, 8, 5))   # Should print 5
    print(x_or_y(5, 34, 12))  # Should print 34
    print(x_or_y(3, 34, 12))  # Should print 34
    print(x_or_y(4, 34, 12))  # Should print 5

C:

    def x_or_y(n, x, y):
        if n <= 1:
            return y
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return y
        return x

    # Testing the function
   