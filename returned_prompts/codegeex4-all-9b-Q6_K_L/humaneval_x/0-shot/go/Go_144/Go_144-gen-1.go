Here is the solution in Go:

```go
func Simplify(x, n string) bool {
    // Split the numerator and denominator of each fraction
    xParts := strings.Split(x, "/")
    nParts := strings.Split(n, "/")

    // Convert the numerator and denominator to integers
    xNumerator, _ := strconv.Atoi(xParts[0])
    xDenominator, _ := strconv.Atoi(xParts[1])
    nNumerator, _ := strconv.Atoi(nParts[0])
    nDenominator, _ := strconv.Atoi(nParts[1])

    // Multiply the numerators and denominators
    numerator := xNumerator * nNumerator
    denominator := xDenominator * nDenominator

    // Check if the resulting fraction is a whole number
    return numerator % denominator == 0
}
```

Explanation:
1. The function `Simplify` takes two string arguments `x` and `n`, which represent fractions.
2. The fractions are split into numerator and denominator using the `/` character as a delimiter.
3. The numerators and denominators are then converted to integers using the `strconv.Atoi` function.
4. The numerators and denominators are multiplied together to get the numerator and denominator of the resulting fraction.
5. The function checks if the resulting fraction is a whole number by checking if the remainder of the numerator divided by the denominator is zero. If it is, the function returns `true`, otherwise it returns `false`.