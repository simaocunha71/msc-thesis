```go
func Simplify(x, n string) bool {
    numeratorX, denominatorX := getNumeratorDenominator(x)
    numeratorN, denominatorN := getNumeratorDenominator(n)

    // Calculate the numerator and denominator of the result
    numeratorResult := numeratorX * numeratorN
    denominatorResult := denominatorX * denominatorN

    // Check if the result is a whole number
    gcd, _ := gcdOfTwoNumbers(denominatorResult, numeratorResult)
    return gcd == numeratorResult
}

func getNumeratorDenominator(frac string) (int, int) {
    parts := strings.Split(frac, "/")
    numerator, _ := strconv.Atoi(parts[0])
    denominator, _ := strconv.Atoi(parts[1])
    return numerator, denominator
}

func gcdOfTwoNumbers(a, b int) (int, error) {
    for b != 0 {
        a, b = b, a%b
    }
    return a, nil
}
```


The idea is to calculate the numerator and denominator of the result of the multiplication of the two fractions, then check if the result is a whole number by finding the greatest common divisor (GCD) of the numerator and the denominator. If the GCD is equal to the numerator, then the result is a whole number. Otherwise, it is not. The `getNumeratorDenominator` function splits the fraction string into numerator and denominator, and the `gcdOfTwoNumbers` function calculates the GCD of two numbers using the Euclidean algorithm. The `Simplify` function uses these two helper functions to simplify the expression.