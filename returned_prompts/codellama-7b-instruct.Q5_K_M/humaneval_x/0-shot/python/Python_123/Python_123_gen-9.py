
def get_odd_collatz(n):
    collatz_seq = []
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        collatz_seq.append(n)
    return sorted(collatz_seq)
