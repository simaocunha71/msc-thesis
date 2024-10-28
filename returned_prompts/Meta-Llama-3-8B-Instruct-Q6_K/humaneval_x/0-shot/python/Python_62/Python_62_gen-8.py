    def derivative(xs: list):
        return [i * x for i, x in enumerate(xs[1:], start=1)]

    print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
    print(derivative([1, 2, 3]))  # Output: [2, 6]  # test cases

    # explanation:
    # The derivative of a polynomial is given by the rule of differentiation, i.e., the derivative of a sum is the sum of the derivatives.
    # In this case, we assume the polynomial is represented as a list of coefficients.
    # The derivative of the polynomial is the sum of the coefficients of the polynomial, each multiplied by the power of x that it represents.
    # We use a list comprehension to generate the derivative.
    # The enumerate function is used to get both the index and the value of each element in the list.
    # The start parameter of the enumerate function is set to 1 to make the index start from 1, because the derivative of the constant term is 0, and we don't want to include it in the result.
    # The result is a new list containing the coefficients of the derivative polynomial.  # test cases

    # The function works as expected and gives the correct results for both test cases.  # test cases
    # It's also worth noting that this function only works for polynomials of degree 4 or less, because it uses a list comprehension to generate the derivative, which can only handle lists of length 5 or less.  # test cases
    # If you need to work with polynomials of higher degree, you would need to use a more complex algorithm or data structure.  # test cases
    # Also, this function assumes that the input list represents a polynomial in the standard form (i.e., the constant term is the first element of the list).  # test cases
    # If the input list represents a polynomial in a different form, you would need to modify the function accordingly.  # test cases
    # In general, this function is a simple and straightforward implementation of the derivative of a polynomial, and it should work correctly for most cases.  # test cases
    # However, it's always a good idea to test your function thoroughly and consider edge cases to ensure it works correctly in all situations.  # test cases
    #