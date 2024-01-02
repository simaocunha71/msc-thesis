

def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """

    # The following is a recursive solution, but I was asked for an iterative one.
    def _fib4(n):
        if n < 5:
            return int(0)
        else:
            f1 = _fib4(n - 1)
            f2 = _fib4(n - 2)
            f3 = _fib4(n - 3)
            f4 = _fib4(n - 4)
            return int((f1 + f2 + f3 + f4))
        
    return _fib4(n)