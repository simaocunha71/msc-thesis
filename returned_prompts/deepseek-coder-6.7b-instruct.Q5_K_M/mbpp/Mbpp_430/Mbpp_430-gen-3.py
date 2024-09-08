"""
The general equation of a parabola is y = a*(x-h)^2 + k, where a is the directrix.
In the given problem, the coefficients of x and y are provided. The coefficient of x^2 will be the directrix.
"""
def parabola_directrix(a,h,k):
    return a*h**2 + k

# Test the function
print(parabola_directrix(5,3,2))

