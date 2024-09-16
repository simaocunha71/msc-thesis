
def count_binary_seq(n):
    return 2**n * (2**n - 1)

# or

def count_binary_seq(n):
    return (2**(2*n) - 1) // (2**n - 1)

# or

def count_binary_seq(n):
    return (2**n) * (2**n - 1)

# or

def count_binary_seq(n):
    return sum(2**i for i in range(2*n+1))
