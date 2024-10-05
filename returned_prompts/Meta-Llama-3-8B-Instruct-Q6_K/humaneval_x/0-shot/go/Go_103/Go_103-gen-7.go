Here is a Go solution for the problem:

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
    return fmt.Sprintf("0b%b", avg)
}
```

This function first checks if `n` is greater than `m`, and if so, returns -1. Then it calculates the sum of the numbers from `n` to `m` (inclusive) using a for loop. After that, it calculates the average of these numbers by dividing the sum by the number of elements (which is `m-n+1`). The `math.Round` function is used to round the average to the nearest integer. Finally, the function converts the average to binary using `fmt.Sprintf` and returns the result. If `n` is greater than `m`, the function returns -1. Otherwise, it returns the binary representation of the rounded average. 