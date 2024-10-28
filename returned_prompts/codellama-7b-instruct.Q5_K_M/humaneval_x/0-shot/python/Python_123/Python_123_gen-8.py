
def get_odd_collatz(n):
    if n <= 0:
        raise ValueError('n should be a positive integer.')
    collatz_seq = [n]
    while collatz_seq[-1] != 1:
        if collatz_seq[-1] % 2 == 0:
            collatz_seq.append(collatz_seq[-1] // 2)
        else:
            collatz_seq.append(3 * collatz_seq[-1] + 1)
    return sorted([num for num in collatz_seq if num % 2 != 0])