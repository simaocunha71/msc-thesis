

def derivative(xs: list):
    return [i*xs[i] for i in range(1,len(xs))]


print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))


Both of these solutions return the derivative of the polynomial. The first solution is simpler but it assumes that the input list has coefficients in order from lowest to highest degree. The second solution is more general and it doesn't assume the order of the input list. It multiplies the coefficient by the degree, then skips the first term (because the derivative of a constant is 0) and returns the rest of the terms.
<jupyter_output>
<empty_output>
<jupyter_text>
