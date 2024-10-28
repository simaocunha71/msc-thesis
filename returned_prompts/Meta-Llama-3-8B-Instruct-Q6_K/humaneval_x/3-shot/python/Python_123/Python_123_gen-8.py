    def collatz(n):
        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            sequence.append(n)
        return sequence

    sequence = collatz(n)
    odd_sequence = [num for num in sequence if num % 2 != 0]
    return sorted(odd_sequence)  # Return the sorted list of odd numbers in the Collatz sequence


