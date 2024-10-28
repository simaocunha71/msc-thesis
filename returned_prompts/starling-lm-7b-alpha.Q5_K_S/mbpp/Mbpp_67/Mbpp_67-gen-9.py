
def bell_number(n: int) -> int:
    bells = [0, 1] + [0] * n
    for i in range(1, n + 1):
        for j in range(i):
            bells[i] += bells[j] * bells[i-j-1]
    return bells[n]


