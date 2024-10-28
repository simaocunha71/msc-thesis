Here is the solution in Go:
```go
package main

import (
    "math"
    "fmt"
)

func SumSquares(lst []float64) int {
    var sum int
    for _, val := range lst {
        // Round each element in the list to the upper int(Ceiling)
        roundedVal := math.Ceil(val)
        sum += int(roundedVal * roundedVal)
    }
    return sum
}

func main() {
    lst := []float64{1, 2, 3}
    fmt.Println(SumSquares(lst))  // Output: 14

    lst = []float64{1, 4, 9}
    fmt.Println(SumSquares(lst))  // Output: 98

    lst = []float64{1, 3, 5, 7}
    fmt.Println(SumSquares(lst))  // Output: 84

    lst = []float64{1.4, 4.2, 0}
    fmt.Println(SumSquares(lst))  // Output: 29

    lst = []float64{-2.4, 1, 1}
    fmt.Println(SumSquares(lst))  // Output: 6
}
```
This program defines a function `SumSquares` that takes a slice of floats as input and returns the sum of squared numbers in the given list, after rounding each element in the list to the upper int(Ceiling) first. In the `main` function, it demonstrates the usage of this function with different input lists. The output of each test case is printed to the console.