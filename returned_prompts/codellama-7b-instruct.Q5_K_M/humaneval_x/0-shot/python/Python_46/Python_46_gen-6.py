

def fib4(n: int) -> int:
    # Initialize the sequence with the first four values
    fib_seq = [0, 0, 2, 0]

    # Iterate through the remaining values in the sequence
    for i in range(4, n+1):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2] + fib_seq[i-3] + fib_seq[i-4])

    return fib_seq[n]