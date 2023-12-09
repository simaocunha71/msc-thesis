

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """

    # Time: O(n), Space: O(n + 3)
    def fibs(n, i, j):
        if n <= 0 or i == j: return 0
        elif n == 1: return (j - i) // (j - i + 2)
        else: return (fibs(n-1, j - 1, j) + fibs(n-2, i - 1, j)) / (j - i + 3)
    def fibfib(n):
        return sum(fibs(i, n - i - 1, n - i - 2) for i in range(0, n))

def fibfib_naive(n: int):
    # Time: O(n), Space: O(n)
    def fibs(n, i):
        if not (i <= 0 or n == 1 and i == n - 2): return 0
        elif i <= 1: return i
        else: return n * n + i
    f = [fibs(i - 1, j) for j in range(i)]
    f.append(-1 if (n - 2) not in f else fibs(-1, (n - 3)))
    ans = sum(f[j] for j in range(0, n)) / (n - 1 + 2)
    return ans

def fib_naive(n: int):
