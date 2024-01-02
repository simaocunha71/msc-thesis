
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """

    return n*n-1, n-1*n+n-1, n-1*n*(n-1)+n-2*n-(n-1),\
        n-1*n*(n-1)*(n-1)+n-3*n-(n-1)-1, \
        ...............
                           , 1,
    """

    """

def special_factorial(input):

    if input > 0:
        return
\end{code}