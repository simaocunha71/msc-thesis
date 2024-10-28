    n := len(xs)
    if n % 2 != 0 {
        panic("FindZero requires a polynomial with even number of coefficients")
    }
    for _, coeff := range xs {
        if coeff != 0 {
            goto B
        }
    }
    panic("FindZero requires a polynomial with non zero coefficients")

B:
    return newton(Poly, xs, float64(n/2))
}

func newton(f func([]int, float64) float64, xs  []int, start float64) float64 {
    x := start
    for i := 0; i < 100; i++ {
        fx := f(xs, x)
        if math.Abs(fx) < 1e-6 {
            return x
        }
        fpx := derivative(f, xs, x)
        if math.Abs(fpx) < 1e-6 {
            continue
        }
        x = x - fx / fpx
    }
    return x
}

func derivative(f func([]int, float64) float64, xs  []int, x float64) float64 {
    h := 1e-6
    return (f(xs, x+h) - f(xs, x)) / h
}
```

The solution is the root of the polynomial using the Newton's method. The `derivative` function calculates the derivative of `f` at point `x`.

In `FindZero`, we first check if all coefficients are zero, if so, we panic. Then we calculate the root using Newton's method.

The `Poly` function calculates the value of the polynomial at point `x`.

The `FindZero` function will only return one root, even if there are many.

The `newton` function uses Newton's method to find a root of the polynomial. It takes the polynomial function `f`, its coefficients `xs`, and the initial guess `start`. It returns the root.

The `derivative` function calculates the derivative of `f` at point `x`. It