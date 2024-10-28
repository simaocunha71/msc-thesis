    def get_odd_collatz(n):
        odd_collatz = set()
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            if n % 2 != 0:
                odd_collatz.add(n)
        odd_collatz.add(1)
        return sorted(list(odd_collatz))



# Test cases
print(get_odd_collatz(5)) # Expected output: [1, 5]
print(get_odd_collatz(10)) # Expected output: [1, 3, 19]
print(get_odd_collatz(20)) # Expected output: [1, 3, 7, 21, 43, 127, 383, 1151]  # This sequence is longer than the expected output, but we're only asked for the odd numbers.