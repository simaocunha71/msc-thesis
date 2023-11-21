

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

    # Time: O(n^3)
    # Memory: O(n^2) (stack)
    sum = 0
    i, j = 1, 1
    while True:
        if n == 1 or n <= 0:
            break
        
        s = i - j + 1
        if s < 0:
            continue
            
        sum += s
        i, j = j-2, j-1
    
    return sum