
def fib4(n: int) -> int:
    # Initialize variables
    a, b, c, d = 0, 0, 0, 0
    # Base case
    if n <= 1:
        return n
    # Initialize array to store Fib4 number sequence
    fib4_seq = [0, 0, 2]
    # Loop through elements in Fib4 number sequence
    for i in range(3, n+1):
        a = b
        b = c
        c = d
        d = fib4_seq[i-1] + fib4_seq[i-2] + fib4_seq[i-3] + fib4_seq[i-4]
        fib4_seq.append(d)
    # Return n-th element of Fib4 number sequence
    return fib4_seq[n]

    # Recursive solution
    if n <= 1:
        return n
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

    # Dynamic programming solution
    if n <= 1:
        return n
    else:
        fib4_seq = [0, 0, 2]
        for i in range(3, n+1):
            fib4_seq.append(fib4_seq[i-1] + fib4_seq[i-2] + fib4_seq[i-3] + fib4_seq[i-4])
        return fib4_seq[n]
