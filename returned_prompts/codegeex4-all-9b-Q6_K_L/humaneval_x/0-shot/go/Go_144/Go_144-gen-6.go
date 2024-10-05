You can solve this problem by converting the fractions into their decimal representation and then checking if the result is a whole number. Here is the code:

```go
import (
    "strconv"
    "strings"
    "math/big"
)

func Simplify(x, n string) bool {
    // Split the fractions into numerator and denominator
    xNum, xDenom := strings.Split(x, "/")[0], strings.Split(x, "/")[1]
    nNum, nDenom := strings.Split(n, "/")[0], strings.Split(n, "/")[1]

    // Convert the numerators and denominators to big.Float
    xNumFloat, _ := new(big.Float).SetString(xNum)
    xDenomFloat, _ := new(big.Float).SetString(xDenom)
    nNumFloat, _ := new(big.Float).SetString(nNum)
    nDenomFloat, _ := new(big.Float).SetString(nDenom)

    // Calculate x * n
    result := new(big.Float).Quo(xNumFloat, xDenomFloat)
    result.Mul(result, nNumFloat)
    result.Quo(result, nDenomFloat)

    // Check if the result is a whole number
    return result.IsInt()
}
```

This code splits the fractions into their numerator and denominator, converts them to `big.Float`, and then calculates `x * n`. Finally, it checks if the result is a whole number by calling the `IsInt` method on the `big.Float` object. If the result is a whole number, the function returns `true`, otherwise it returns `false`.