
def tri(n):
    seq = [3]
    if n < 2:
        return seq
    seq += [1 + n / 2] * (n // 2 + 1)
    for i in range(n):
        if i % 6 == 0:
            seq += [seq[-3] + seq[-2] + seq[-1]]
        else:
            if i % 3 == 1:
                seq += [seq[-2] + seq[-1] + seq[i + 1]]
            else:
                seq += [seq[-1] + seq[i + 1]]
    return seq


# Another solution:

def tri(n):
    """
    >>> tri(3)
    [1, 3, 2, 8]
    >>> tri(4)
    [1, 3, 2, 8, 13, 21, 34, 55]
    >>> tri(10)
    [1, 3, 2, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    """
    if n == 0:
        return []
    seq = [1, 3]
    while len(seq) <= n:
        seq += [seq[-2] + seq[-1] + seq[-3]]
    return seq[:n+1]


# Another solution:

def tri(n):
    seq = [3]
    if n == 0:
        return seq
    elif n == 1:
        return seq
    else:
        for _ in range(n):
            seq += [seq[-1] + seq[-2] + seq[-3]]
    return seq[:n+1]


# Another solution:

def tri(n):
    """
    >>> tri(3)
    [1, 3, 2, 8]
    >>> tri(4)
   