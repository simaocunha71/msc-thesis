

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * (1 / 2) ** 2 + h/2

def square_area(a):
    """Find the area of a square
    >>> square_area(4)
    64
    """
    return a * a

def area(p, q, r, h):
    # If all sides are equal to each other then we can simplify this 
    if (p == q and q == r):
        return triangle_area((q+h)/2, (r-h)/2)
    
    elif (p > 0 and q < 0 and r >= p):
        area = square_area(abs(p)) + triangle_area(abs(q), abs(r))
        
    else:
        raise ValueError('Cannot Calculate Area')

# Example of using the function above
area(6, -12, 7)