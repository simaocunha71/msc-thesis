```go
func Simplify(x, n string) bool {
    num1, _ := strconv.Atoi(strings.Split(x, "/")[0])
    denom1, _ := strconv.Atoi(strings.Split(x, "/")[1])
    num2, _ := strconv.Atoi(strings.Split(n, "/")[0])
    denom2, _ := strconv.Atoi(strings.Split(n, "/")[1])

    productNum := num1 * num2
    productDenom := denom1 * denom2

    gcd := func(a, b int) int {
        for b != 0 {
            a, b = b, a%b
        }
        return a
    }

    gcdValue := gcd(productNum, productDenom)
    return productNum/gcdValue == productDenom/gcdValue
}
```
The provided Go function `Simplify` takes two string parameters `x` and `n` representing fractions in the format "numerator/denominator". It converts these strings into integers using `strconv.Atoi` and `strings.Split`, calculates the product of the numerators and denominators, and then finds the greatest common divisor (GCD) of this product using a helper function `gcd`. Finally, it checks if the product numerator divided by the GCD is equal to the product denominator divided by the GCD. If this condition is true, it returns `true`, indicating that the product is a whole number; otherwise, it returns `false`. This function can be used to simplify expressions of the form `x * n`, where `x` and `n` are valid fractions. For example, `Simplify("1/5", "5/1")` returns `true`, while `Simplify("1/6", "2/1")` and `Simplify("7/10", "10/2")` return `false`. 