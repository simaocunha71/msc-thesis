Here is the solution in Go:
```go
package main

import (
    "math"
    "fmt"
)

func SumSquares(lst []float64) int {
    var sum int
    for _, v := range lst {
        // Round each element to the upper int(Ceiling)
        rounded := math.Ceil(v)
        sum += int(rounded * rounded)
    }
    return sum
}

func main() {
    fmt.Println(SumSquares([]float64{1, 2, 3}))  // Output: 14
    fmt.Println(SumSquares([]float64{1, 4, 9}))  // Output: 98
    fmt.Println(SumSquares([]float64{1, 3, 5, 7}))  // Output: 84
    fmt.Println(SumSquares([]float64{1.4, 4.2, 0}))  // Output: 29
    fmt.Println(SumSquares([]float64{-2.4, 1, 1}))  // Output: 6
}
```
This function iterates over the input list, rounds each element to the upper integer using the `math.Ceil` function, squares the rounded element, and adds it to the sum. The final sum is returned as an integer. In the `main` function, we test the `SumSquares` function with different input lists and print the results.