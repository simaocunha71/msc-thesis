```go
func Simplify(x, n string) bool {
    numeratorX, denominatorX := strconv.Atoi(strings.Split(x, "/")[0]), strconv.Atoi(strings.Split(x, "/")[1])
    numeratorN, denominatorN := strconv.Atoi(strings.Split(n, "/")[0]), strconv.Atoi(strings.Split(n, "/")[1])

    productNumerator, _ := strconv.Atoi(strconv.Itoa(numeratorX * numeratorN))
    productDenominator, _ := strconv.Atoi(strconv.Itoa(denominatorX * denominatorN))

    gcd := GCD(productNumerator, productDenominator)
    return productNumerator/gcd == productDenominator/gcd
}

func GCD(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}
```

Explanation:
The function `Simplify` takes two string representations of fractions `x` and `n` and returns a boolean indicating whether their product is a whole number or not.

First, it extracts the numerators and denominators from `x` and `n` using `strings.Split` and `strconv.Atoi`. Then, it calculates the product of the numerators and denominators, and finds the greatest common divisor (GCD) of the product using the `GCD` function.

Finally, it checks whether the product is a whole number by verifying whether the product numerator divided by the GCD is equal to the product denominator divided by the GCD. If this condition is true, the function returns `true`; otherwise, it returns `false`.

The `GCD` function is a simple implementation of the Euclidean algorithm, which calculates the GCD of two numbers by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b` until `b` becomes zero. The GCD is then returned as `a`.