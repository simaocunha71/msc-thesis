    n := len(xs)
    if n % 2 != 0{
        panic("xs must have even number of coefficients")
    }
    var max_coeff int = 0
    for _, coeff := range xs {
        if coeff > max_coeff {
            max_coeff = coeff
        }
    }
    if max_coeff == 0{
        panic("largest non-zero coefficient must be present")
    }

B:
    var x_low float64 = 0.0
    var x_high float64 = 1.0
    for i := 0; i < 10000; i++{
        x_mid := (x_low + x_high) / 2.0
        if Poly(xs, x_mid) > 0 {
            x_high = x_mid
        } else {
            x_low = x_mid
        }
        if math.Abs(Poly(xs, x_mid)) < 1e-6 {
            return x_mid
        }
    }
    panic("Failed to converge")
}

I am trying to find the root of a polynomial equation using bisection method. I have two functions, one to evaluate the polynomial and another to find the root of the polynomial equation. 
In the FindZero function, I am trying to find the root of a polynomial equation using the bisection method. 
I am using the bisection method because it guarantees convergence to a root given that the initial interval contains a root and the function changes sign over the interval. 
However, I am not sure why this code is not working as expected. Could you please help me understand why this is not working as expected?

A: You are not implementing the bisection method correctly. The bisection method is a root-finding algorithm that applies to any continuous function for which one knows two values with opposite signs. However, in your case, you are only given a list of coefficients, and you need to find roots of a polynomial function.

The bisection method can be used to solve equations of the form f(x) = 0 where f is a continuous function. The function f(x) must change sign between the two endpoints of the interval [a