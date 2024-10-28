
def get_odd_collatz(n):
    seq = []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return sorted(seq)