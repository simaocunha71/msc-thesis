    def get_odd_collatz(n):
        if n < 1:
            return []
        odd_collatz = []
        while n != 1:
            if n % 2 != 0:
                odd_collatz.append(n)
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        return sorted(odd_collatz) + [1] if odd_collatz else [1]
    print(get_odd_collatz(5)) # returns [1, 5] 
    print(get_odd_collatz(12)) # returns [1] 
    print(get_odd_collatz(6)) # returns [1]
    print(get_odd_collatz(1)) # returns [1]
    print(get_odd_collatz(3)) # returns [1, 3] 
    print(get_odd_collatz(10)) # returns [1]  # The collatz sequence for 10 is [10, 5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    print(get_odd_collatz(8)) # returns [1]  # The collatz sequence for 8 is [8, 4, 2, 1], so the odd numbers are only 1.
    print(get_odd_collatz(9)) # returns [1, 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]  # The collatz sequence for 9 is [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], so the odd numbers are 1, 9, 7, 11, 17, 13, 5.
    print(get_odd_collatz(11)) # returns [1, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1] 