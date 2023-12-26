
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

    n = int(n)
    if x.count("/"):
        x = str(x[:-1]) + ""
        y = str(y[1:])
    else:
        y = str(x)

    n_int, n_denom, denom_str, remainder = divmod(n, 1)
    x_int, x_denom, denom_str2, remainder2 = divmod(x, denominator(x))

    if (n >= 0 and x >= 0):
        int_n, int_x = int(n), int(x)

        # If both numbers are zero, the result is also a whole number.
        if (int_n == int_x): return True

        # Otherwise, if either of them is negative or is not a valid fraction, we will have to do
        # some more checking before deciding what the answer should be.
        elif (-1 < denom(n)) and (-1 < denominator(x)):
            n = n * (int(round(denom(int_n), 0))) + remainder2
            x = x * ((int) round(denom(int_x), 0))
        elif int(abs(denom(n))) > abs(denom(x)): # If the denominator of n is larger than that of x, we have to make sure that
            # x is smaller than n.
            if ((n - remainder2) * (int(round(