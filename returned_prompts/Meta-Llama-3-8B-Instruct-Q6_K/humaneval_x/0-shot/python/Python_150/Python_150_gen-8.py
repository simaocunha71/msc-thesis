    def x_or_y(n, x, y):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    return y
            return x
        else:
            return y
    # Test cases
    print(x_or_y(7, 34, 12))  # Should print: 34
    print(x_or_y(15, 8, 5))   # Should print: 5
    print(x_or_y(2, 34, 12))  # Should print: y
    print(x_or_y(23, 34, 12)) # Should print: 34
    print(x_or_y(4, 34, 12))  # Should print: y
    print(x_or_y(13, 34, 12)) # Should print: 34
    print(x_or_y(10, 34, 12)) # Should print: y
    print(x_or_y(11, 34, 12)) # Should print: 34

B:

    def x_or_y(n, x, y):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    return y
            return x
        else:
            return y
    # Test cases
    print(x_or_y(7, 34, 12))  # Should print: 34
    print(x_or_y(15, 8, 5))   # Should print: 5
    print(x_or_y(2, 34, 12))  # Should print: 12
    print(x_or_y(23, 34, 12)) # Should print: 34
    print(x_or_y(4, 34, 12))  # Should print: 12
    print(x_or_y(13, 34, 12)) # Should print: 34
    print(x_or_y(10, 34, 12)) # Should print: 12
    print(x_or_y(11, 34, 12)) # Should print: 34
    print(x_or_y(1, 34, 12))  # Should print: 12

C:

    def x_or_y(n, x, y):
        if n > 1:
            for i in range(2, n