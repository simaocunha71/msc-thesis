
def solve(N):
    if N == 0: return '0'
    s = ''
    while N:
        s = str(N % 2) + s
        N //= 2
    return s
