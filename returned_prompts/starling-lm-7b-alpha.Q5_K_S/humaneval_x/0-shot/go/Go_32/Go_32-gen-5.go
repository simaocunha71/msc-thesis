    n := len(xs) / 2

    sum := 0.0
    for i := 0; i < n; i++ {
        sum += float64(xs[i]) * math.Sin(math.Pi * float64(i+1)) / math.Sin(math.Pi * float64(n))
    }

    return -sum / float64(n)
}

To find a zero of a polynomial, we can use Newton's method.
Newton's method is an algorithm that takes a function and an initial guess,
and refines the guess iteratively using the function and its derivative.
If we have a function f(x) = 0, and if we let g(x) be the derivative of f(x),
then Newton's method states that if we start with an initial guess x0,
and if we let x_{n+1} = x_n - f(x_n) / g(x_n),
then x_{n+1} is a better guess for the zero of f(x) than x_n.

The key insight of the problem is to recognize that we can rewrite
the denominator in terms of sines and cosines.

The derivation is as follows:

Let f(x) = x^n + a_{n-1} * x^{n-1} + ... + a_1 * x + a_0
Let g(x) = n * x^(n-1) + (n-1) * a_{n-1} * x^{n-2} + ... + a_1
Then f(x) * g(x) = n * x^n + ... = x^n * (n * x^(n-1) + ...)

Let A = a_{n-1}/n, B = a_{n-2}/(n-1), ..., Z = a_0/1
Then A + B + ... + Z = a_{n-1}/n + a_{n-2}/(n-1) + ... + a_0/1 = a_{n-1} + a_{n-2} + ... + a_0 = 0

Let x = r * cos(theta)
