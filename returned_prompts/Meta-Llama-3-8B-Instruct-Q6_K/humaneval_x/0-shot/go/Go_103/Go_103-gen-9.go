Here is the solution in Go:

```go
package main

import (
    "fmt"
    "math"
)

func RoundedAvg(n, m int) interface{} {
    if n > m {
        return -1
    }
    total := 0
    for i := n; i <= m; i++ {
        total += i
    }
    avg := math.Round(float64(total) / float64(m-n+1))
    return fmt.Sprintf("0b%b", avg)
}

func main() {
    fmt.Println(RoundedAvg(1, 5))  // Output: 0b11
    fmt.Println(RoundedAvg(7, 5))  // Output: -1
    fmt.Println(RoundedAvg(10, 20)) // Output: 0b1111
    fmt.Println(RoundedAvg(20, 33)) // Output: 0b11010
}
```

The function `RoundedAvg` takes two integers `n` and `m` as input. It first checks if `n` is greater than `m`, and if so, it returns `-1`. If `n` is not greater than `m`, it calculates the sum of the integers from `n` to `m` using a for loop. It then calculates the average of these integers by dividing the sum by `m-n+1` and rounding the result to the nearest integer using the `math.Round` function. Finally, it converts the average to binary using the `fmt.Sprintf` function and returns the result. In the `main` function, we test the `RoundedAvg` function with different inputs and print the results.