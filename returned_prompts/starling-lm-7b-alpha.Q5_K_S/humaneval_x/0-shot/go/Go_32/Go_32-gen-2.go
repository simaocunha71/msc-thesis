    if len(xs) % 2 != 0 {
        return 0
    }
    n := len(xs) / 2
    coeff := make([]int, n)
    for i := 0; i < n; i++ {
        coeff[i] = xs[i*2+1]
    }
    x := Poly(coeff, -xs[0]/float64(xs[1]))
    return x
}

To find the zero point of a polynomial, we can use Newton's method.

Here's an example to illustrate Newton's method:

f(x) = 3x^4 + 3x^3 + 1
f'(x) = 12x^3 + 9x^2

To use Newton's method, we start with an initial guess for the zero point. Here, we'll use x = 1 as our initial guess.

The formula for Newton's method is:

x_new = x_old - f(x_old) / f'(x_old)

We'll use this formula to update our guess until we reach a point where the difference between the old and new guesses is very small. This indicates that we have found a zero point.

Here's the step-by-step process using Newton's method:

1. Start with an initial guess for the zero point, x_old = 1.
2. Calculate f(x_old) = 3(1)^4 + 3(1)^3 + 1 = 8.
3. Calculate f'(x_old) = 12(1)^3 + 9(1)^2 = 21.
4. Update our guess using the Newton's method formula: x_new = x_old - f(x_old) / f'(x_old) = 1 - 8 / 21 = 0.4762.
5. Repeat steps 2-4 until the difference between the old and new guesses is very small.

Using Newton's method, we find that the zero point of the polynomial f(x) = 3x^4 + 3x^3 + 1 is approximately x = 0.47