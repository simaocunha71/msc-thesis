```go
func Simplify(x, n string) bool {
    // Parse the fractions
    xNum, _ := strconv.Atoi(strings.Split(x, "/")[0])
    xDen, _ := strconv.Atoi(strings.Split(x, "/")[1])
    nNum, _ := strconv.Atoi(strings.Split(n, "/")[0])
    nDen, _ := strconv.Atoi(strings.Split(n, "/")[1])

    // Calculate the numerator and denominator of the result
    resultNum := xNum * nNum
    resultDen := xDen * nDen

    // Check if the result is a whole number
    if resultDen == 1 {
        return true
    }

    // Check if the result has a common factor with the denominator
    for i := 2; i <= math.Min(float64(resultNum), float64(resultDen)); i++ {
        if resultNum%i == 0 && resultDen%i == 0 {
            resultNum /= i
            resultDen /= i
        }
    }

    // Check if the result is a whole number
    if resultDen == 1 {
        return true
    }

    return false
}
```A

In this solution, we first parse the input fractions into their numerator and denominator using the `strconv.Atoi` function. Then, we calculate the numerator and denominator of the result by multiplying the corresponding numerators and denominators.

Next, we check if the result is a whole number by checking if the denominator is 1. If it is, we return `true`.

If the result is not a whole number, we then check if it has a common factor with the denominator by iterating from 2 to the minimum of the numerator and denominator. If we find a common factor, we divide both the numerator and denominator by that factor.

Finally, we check again if the result is a whole number. If it is, we return `true`. Otherwise, we return `false`.A

This solution assumes that the input fractions are valid and do not have zero as a denominator. It also assumes that the result of the multiplication is a valid fraction. In practice, you may want to add error handling to handle invalid input or overflow errors.