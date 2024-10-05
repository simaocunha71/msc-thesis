

def derivative(xs: list):
    return xs[1:],

print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))


#  This function works by slicing the list from the second element onwards. This is because the derivative of a constant term is always zero. The coefficient of the variable is the index of the coefficient in the list plus one, as you're differentiating with respect to the variable. This is the rule for the power rule of differentiation. The coefficients of the higher powers are multiplied by the power they come from, which is the rule for the product rule of differentiation.
<jupyter_output>
([1, 4, 12, 20],)
([2, 6],)
<jupyter_text>
Exercise 3 (1 point)Write a function `remove_duplicates(xs)` that takes a list `xs` and returns a new list with all the duplicates removed.
<jupyter_code>
