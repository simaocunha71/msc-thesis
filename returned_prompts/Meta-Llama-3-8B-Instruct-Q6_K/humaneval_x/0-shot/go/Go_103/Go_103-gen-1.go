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
    sum := 0
    for i := n; i <= m; i++ {
        sum += i
    }
    avg := math.Round(float64(sum) / float64(m-n+1))
    binary := fmt.Sprintf("%b", int(avg))
    return binary
}

func main() {
    fmt.Println(RoundedAvg(1, 5))  // "0b11"
    fmt.Println(RoundedAvg(7, 5))  // -1
    fmt.Println(RoundedAvg(10, 20)) // "0b1111"
    fmt.Println(RoundedAvg(20, 33)) // "0b11010"
}
```


Explanation:

1. We first check if `n` is greater than `m` and return -1 if it is.
2. We calculate the sum of the integers from `n` to `m` using a for loop.
3. We calculate the average by dividing the sum by the number of integers (`m-n+1`).
4. We use the `math.Round` function to round the average to the nearest integer.
5. We convert the rounded average to binary using the `fmt.Sprintf` function with the format string `%b`.
6. We return the binary string as the result.

In the `main` function, we test the `RoundedAvg` function with the provided examples and print the results.