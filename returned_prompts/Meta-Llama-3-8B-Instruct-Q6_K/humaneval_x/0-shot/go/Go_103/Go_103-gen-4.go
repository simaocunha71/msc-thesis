Here is the Go function that implements the described behavior:

```go
import (
    "fmt"
    "math"
)

func RoundedAvg(n, m int) interface{} {
    if n > m {
        return -1
    }
    sum := 0
    for i := n; i <= m; i++ {
        sum += i
    }
    avg := math.Round(float64(sum) / float64(m-n+1))
    binary := fmt.Sprintf("%b", int(avg))
    return binary
}
```

This function first checks if `n` is greater than `m` and returns `-1` if true. Then it calculates the sum of integers from `n` to `m` and divides it by `m-n+1` to get the average. The `math.Round` function is used to round the average to the nearest integer. Finally, the average is converted to binary using the `fmt.Sprintf` function and the `%b` format specifier, which converts an integer to binary. The resulting binary string is returned as the result.