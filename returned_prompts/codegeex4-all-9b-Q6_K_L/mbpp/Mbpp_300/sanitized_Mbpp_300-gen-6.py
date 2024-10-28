def count_binary_seq(n):
    if n == 1:
        return 2

    # Count the number of binary sequences of length 2(n-1) such that the sum of the first (n-1) bits is the same as the sum of the last (n-1) bits
    count = count_binary_seq(n-1)

    # Multiply the count by 2 (since we can add either a 0 or a 1 to the sequence)
    count *= 2

    return count