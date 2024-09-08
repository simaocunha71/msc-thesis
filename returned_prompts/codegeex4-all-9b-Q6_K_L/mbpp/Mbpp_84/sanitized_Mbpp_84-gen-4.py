def sequence(n):
    """
    The Newman Conway sequence is a sequence of integers that starts with 1, 2, and 3.
    Each subsequent number in the sequence is the sum of the previous two numbers in the sequence.
    The nth number in the sequence is the sum of the (n-1)th and (n-2)th numbers in the sequence.
    """
    sequence = [1, 2, 3]
    for i in range(3, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[n-1]