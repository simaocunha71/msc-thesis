
def fibfib(n):
    if n in [0, 1]:
        return n
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
