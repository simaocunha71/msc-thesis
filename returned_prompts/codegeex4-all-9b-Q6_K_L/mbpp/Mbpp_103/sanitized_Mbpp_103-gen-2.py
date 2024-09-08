def eulerian_num(n, m):
    """
    This function calculates the Eulerian number a(n, m) using the formula:
    a(n, m) = (m+n-2)! / ((m-1)! * (n-1)!)
    """
    from math import factorial
    return factorial(m+n-2) // (factorial(m-1) * factorial(n-1))