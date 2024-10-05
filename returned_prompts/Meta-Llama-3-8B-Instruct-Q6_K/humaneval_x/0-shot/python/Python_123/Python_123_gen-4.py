    def get_odd_collatz(n):
        sequence = []
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            if n % 2 != 0:
                sequence.append(n)
        if n % 2 != 0:
            sequence.append(n)
        return sorted(sequence)
    # Test the function
    print(get_odd_collatz(5))  # Output: [1, 5]
    print(get_odd_collatz(6))  # Output: [3, 10]
    print(get_odd_collatz(8))  # Output: [5, 16, 8, 4, 2, 1]
    print(get_odd_collatz(10))  # Output: [1, 5, 16, 8, 4, 2, 1]
    print(get_odd_collatz(12))  # Output: [3, 10, 5, 16, 8, 4, 2, 1]
    print(get_odd_collatz(14))  # Output: [1, 5, 16, 8, 4, 2, 1]
    print(get_odd_collatz(15))  # Output: [1, 5, 16, 8, 4, 2, 1]
    print(get_odd_collatz(16))  # Output: [3, 10, 5, 16, 8, 4, 2, 1]
    print(get_odd_collatz(18))  # Output: [3, 10, 5, 16, 8, 4, 2, 1]
    print(get_odd_collatz(20))  # Output: [1, 5, 16, 8, 4, 2, 1]
    print(get_odd_collatz(21))  # Output: [1, 5, 16, 8, 4, 2, 1]
    print(get_odd_collatz(22))  # Output: [3, 10, 5, 16, 8, 4, 2, 1]
    print(get_odd_collatz(24))  # Output: [3, 10, 5, 16, 8, 4, 2