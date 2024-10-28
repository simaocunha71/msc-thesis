In the PolynomialEvaluation.main method, we are testing if the poly method can correctly evaluate a polynomial with coefficients xs at a point x. We are also testing if the findZero method can find the zero of a polynomial with even number of coefficients.

The findZero method is a bit tricky to understand. It works as follow:

1. It initializes x = -result / xs[0] as the initial guess of the zero of the polynomial.
2. Then it initializes a new list of coefficients, newXs, by subtracting the multiplication of the index and x from each coefficient. It is equivalent to (xs[1] - xs[0] * i, xs[2] - xs[1] * i, ... , xs[n] - xs[n-1] * i).
3. It checks if the size of newXs is odd, if it is, it goes back to the beginning of the while loop (