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
    return sorted([num for num in sequence if num % 2 != 0])  # return the odd numbers in the sequence, sorted in increasing order.  # return [num for num in sequence if num % 2 != 0]  # return the odd numbers in the sequence


