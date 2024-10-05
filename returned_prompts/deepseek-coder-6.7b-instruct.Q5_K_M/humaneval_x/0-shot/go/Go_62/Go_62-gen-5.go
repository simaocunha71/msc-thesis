
    ys := make([]int, len(xs) - 1)
    for i := 1; i < len(xs); i++ {
        ys[i-1] = xs[i] * i
    }
    return ys
}

func main() {
    fmt.Println(Derivative([]int{3, 1, 2, 4, 5}))
    fmt.Println(Derivative([]int{1, 2, 3}))
}

```

The function `Derivative(xs []int) []int` takes an array of integers `xs` representing the coefficients of a polynomial. It returns a new array `ys` which represents the derivative of the polynomial. The derivative of a polynomial is calculated by multiplying each coefficient by its power and then subtracting 1. So, for example, if the input polynomial is `xs[0] + xs[1] * x + xs[2] * x^2 + ....`, then the output polynomial `ys[0] + ys[1] * x + ys[2] * x^2 + ....` will be the derivative of the input polynomial.

The function `Derivative` loops through the coefficients of the polynomial starting from the second one (index 1), multiplies each coefficient by its index (power), and adds the result to the new array `ys`. This effectively calculates the derivative of the polynomial. Finally, it returns the new array `ys`.

In the `main` function, the `Derivative` function is called with two test cases. The results are printed to the console.
