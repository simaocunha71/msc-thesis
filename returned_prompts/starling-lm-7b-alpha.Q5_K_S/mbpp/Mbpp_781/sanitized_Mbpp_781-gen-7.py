def count_divisors(n):
    # Initialize result
    result = 0
    # Note that this loop runs till square root
    i = 1
    while i <= math.sqrt(n):
        if (n % i == 0):
            # If divisors are equal,
            # count only one
            if (n / i == i):
                result = result + 1
            else: # Otherwise count both
                result = result + 2
        i = i + 1
    return result