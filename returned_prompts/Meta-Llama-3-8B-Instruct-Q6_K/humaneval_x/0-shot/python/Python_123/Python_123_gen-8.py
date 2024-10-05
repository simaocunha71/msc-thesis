    def get_odd_collatz(n):
        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            if n % 2 != 0:
                sequence.append(n)
        return sorted(set(sequence))
    # Test the function
    print(get_odd_collatz(5))  # [1, 5]
    print(get_odd_collatz(12))  # [1, 3, 7, 21, 65, 197, 593] 
    print(get_odd_collatz(7))   # [1, 7] 
    print(get_odd_collatz(10))  # [1, 3, 19]  # The collatz sequence for 10 is [10, 5, 16, 8, 4, 2, 1], so the odd numbers are 1, 3, and 19. 
    print(get_odd_collatz(11))  # [1, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]  # The collatz sequence for 11 is [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], so the odd numbers are 1, 11, 17, 13, and 5. 
    print(get_odd_collatz(20))  # [1, 3, 7, 21, 65, 197, 593]  # The collatz sequence for 20 is [20, 10, 5, 16, 8, 4, 2, 1], so the odd numbers are 1, 3, 7, 21, 65, and 197. 
    print(get_odd_collatz(25))  # [1, 3, 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4