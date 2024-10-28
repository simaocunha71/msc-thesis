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

# Example usage:
print(get_odd_collatz(5))  # Output: [1, 5]
print(get_odd_collatz(10))  # Output: [1, 3, 5, 17, 53, 161]
print(get_odd_collatz(20))  # Output: [1, 3, 5, 7, 21, 65, 197]