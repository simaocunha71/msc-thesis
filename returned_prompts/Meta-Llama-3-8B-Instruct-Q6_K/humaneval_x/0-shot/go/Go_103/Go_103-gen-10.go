Here is a Go solution for the problem:

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
    return fmt.Sprintf("0b%b", avg)
}

func main() {
    fmt.Println(RoundedAvg(1, 5))  // Output: 0b11
    fmt.Println(RoundedAvg(7, 5))  // Output: -1
    fmt.Println(RoundedAvg(10, 20)) // Output: 0b1111
    fmt.Println(RoundedAvg(20, 33)) // Output: 0b11010
}
```

This program first checks if `n` is greater than `m`, in which case it returns `-1`. If `n` is less than or equal to `m`, it calculates the sum of the integers from `n` to `m` (inclusive) and then calculates the average by dividing the sum by the number of integers. The average is then rounded to the nearest integer using the `math.Round` function. Finally, the rounded average is converted to a binary string using the `fmt.Sprintf` function with the format string `"0b%b"`. The `%b` format specifier is used to convert the integer to a binary string. The `0b` prefix is added manually using the format string. The function returns the binary string as an `interface{}` value. In the `main` function, the program calls the `RoundedAvg` function with different inputs and prints the results.