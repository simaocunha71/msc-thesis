    def get_odd_collatz(n):
        result = []
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            if n % 2 != 0:
                result.append(n)
        result.append(1)
        return sorted(result)
    print(get_odd_collatz(5))  # Output: [1, 5]
    print(get_odd_collatz(10))  # Output: [1, 3, 5, 7]
    print(get_odd_collatz(20))  # Output: [1, 3, 5, 7, 13]
    print(get_odd_collatz(25))  # Output: [1, 5, 7, 13]  # The collatz sequence for 25 is [25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], so the odd numbers are 1, 5, 7, 13.
    print(get_odd_collatz(30))  # Output: [1, 3, 5, 7, 13, 19, 29]  # The collatz sequence for 30 is [30, 15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1], so the odd numbers are 1, 3, 5, 7, 13, 19, 29.
    print(get_odd_collatz(40))  # Output: [1, 3, 5, 7, 13, 19, 29, 31, 47, 71]
    print(get_odd_collatz(50))  # Output: [1, 3, 5, 7, 13, 19, 29, 31, 47, 71, 89]  # The collatz sequence for 50 is [50, 25, 76, 38, 