
The problem asks you to find the average of a range of integers, round it to the nearest integer, and convert the result to binary.

Here's a solution in Go:

```go
package main

import (
    "fmt"
    "math"
)

func RoundedAvg(n, m int) string {
    if n > m {
        return "-1"
    }
    sum := 0
    for i := n; i <= m; i++ {
        sum += i
    }
    avg := math.Round(float64(sum) / float64(m-n+1))
    return fmt.Sprintf("%b", int(avg))
}

func main() {
    fmt.Println(RoundedAvg(1, 5))  // Output: 0b11
    fmt.Println(RoundedAvg(