    # Initialize a list to store the fibonacci series
    fib = [0, 0, 2]

    # n is greater than 2
    for i in range(3, n + 1):
        fib.append(fib[i - 3] + fib[i - 2] + fib[i - 1])

    # return the n-th term of fibonacci series
    return fib[n]


