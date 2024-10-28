def catalan_number(n):
    # Catalan number is defined as
    # C(n) = (2n)! / ((n+1)! * n!)
    return (fact(2*n))//(fact(n+1) * fact(n))
def fact(n):
    # Factorial function
    result = 1
    while (n != 1):
        result *= n
        n -= 1
    return result