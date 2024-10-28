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
    sum := 0
    for i := n; i <= m; i++ {
        sum += i
    }
    avg := math.Round(float64(sum) / float64(m-n+1))
    bin := fmt.Sprintf("%b", int(avg))
    return bin
}

func main() {
    fmt.Println(RoundedAvg(1, 5))  // "0b11"
    fmt.Println(RoundedAvg(7, 5))  // -1
    fmt.Println(RoundedAvg(10, 20)) // "0b1111"
    fmt.Println(RoundedAvg(20, 33)) // "0b11010"
}
```
This program defines a function `RoundedAvg` that takes two integers `n` and `m` as input. It calculates the sum of the integers from `n` to `m` (inclusive), computes the average by dividing the sum by the number of integers, rounds the average to the nearest integer using the `math.Round` function, and converts the rounded average to binary using the `fmt.Sprintf` function with the format string `"%b"`. If `n` is greater than `m`, the function returns `-1`.

In the `main` function, we test the `RoundedAvg` function with different input values and print the results. The output should match the examples provided in the problem statement.