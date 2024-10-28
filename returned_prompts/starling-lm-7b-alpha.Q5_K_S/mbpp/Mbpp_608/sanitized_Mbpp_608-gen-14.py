def bell_Number(n: int) -> int:
    if n == 0:
        return 1
    else:
        return bell_Number(n-1) + h_num(n-1, n-1)
def h_num(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    else:
        return h_num(n, k-1) * (n-k+1) // k