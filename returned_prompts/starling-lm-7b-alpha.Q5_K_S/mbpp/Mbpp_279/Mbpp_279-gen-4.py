def is_num_decagonal(n):
    if (n > 0 and n % 1 == 0):
        return True
    else:
        return False

def nth_decagonal_number(n):
    if is_num_decagonal(n):
        return (11*n*(n+1) // 2) + 1
    else:
        return "N is not a positive integer"

# test
print(nth_decagonal_number(3))




"""
The nth decagonal number is the number of dots in the nth decagon. The first few decagonal numbers are:
1, 11, 27, 55, 91, ...
The general formula for the nth decagonal number is:
n * (n + 1) * (11 + 9 * (n - 1)) / 2
"""

"""
A decagon is a polygon with 10 sides. The sum of the interior angles of any decagon is given by:
(n - 2) * 180 degrees, where n is the number of sides.
The formula for the area of a regular decagon is given by:
(n / 2) * (1 + sqrt(5)) * (side length)^2
The formula for the perimeter of a regular decagon is given by:
10 * (side length)
"""

"""
The nth decagonal number is the number of dots in the nth decagon. The first few decagonal numbers are:
1, 11, 27, 55, 91, ...
The general formula for the nth decagonal number is:
n * (n + 1) * (11 + 9 * (n - 1)) / 2
"""

"""
A decagon is a polygon with 10 sides. The sum of the interior angles of any decagon is given by:
(n - 2) * 180 degrees, where n is the number of sides.
The formula for the area of a regular decagon is given by:
(n / 2) * (1 + sqrt(5)) * (side length)^2
The formula