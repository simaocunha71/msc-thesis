    def solve(N):
        binary_list = []
        while N > 0:
            binary_list.append(N % 2)
            N //= 2
        return "".join(map(str, binary_list[::-1]))

# ----------------------------------------------------------------------------

def solve_sol(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.
    """
    binary_list = []
    while N > 0:
        binary_list.append(N % 2)
        N //= 2
    return "".join(map(str, binary_list[::-1]))

# ----------------------------------------------------------------------------

def solve_sol2(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.
    """
    return bin(N)[2:].zfill(8)

# ----------------------------------------------------------------------------

def solve_sol3(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.
    """
    if N == 0:
        return "0"
    return str(bin(N)[2:])

# ----------------------------------------------------------------------------

def solve_sol4(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.
    """
    return format(N, "b")

# ----------------------------------------------------------------------------

def solve_sol5(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.
    """
    return "{0:b}".format(N)

# ----------------------------------------------------------------------------

def solve_sol6(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.
    """
    return format(N, "08b")

# ----------------------------------------------------------------------------

def solve_sol7(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.
    """
    return "{0:08b}".format(N)