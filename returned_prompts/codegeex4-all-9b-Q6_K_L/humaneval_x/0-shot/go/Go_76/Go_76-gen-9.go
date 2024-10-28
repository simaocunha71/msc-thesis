You can use the math package to check if a number is a simple power of another. Here's how you can do it:

```go
import "math"

func IsSimplePower(x int, n int) bool {
    if n == 1 {
        return x == 1
    }
    power := math.Pow(float64(n), math.Log(float64(x))/math.Log(float64(n)))
    return power == math.Round(power)
}
```

Explanation:
- If `n` is 1, then `x` must be 1 for it to be a simple power.
- Calculate `power` by using the `math.Pow` function to raise `n` to the power of `math.Log(x)/math.Log(n)`. This is equivalent to finding the `n`th root of `x`.
- If `power` is equal to its rounded value, then `x` is a simple power of `n`.