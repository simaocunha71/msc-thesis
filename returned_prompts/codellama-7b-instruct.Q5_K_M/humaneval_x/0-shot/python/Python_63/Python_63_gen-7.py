
def fibfib(n: int):
    # Write your code here.
    if n == 0 or n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

