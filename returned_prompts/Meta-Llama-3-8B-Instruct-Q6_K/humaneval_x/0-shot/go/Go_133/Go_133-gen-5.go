Here is the solution in Go language:
```go
package main

import (
    "math"
    "fmt"
)

func SumSquares(lst []float64) int {
    var sum int
    for _, num := range lst {
        // Round the number to the upper int using Ceiling function
        rounded := math.Ceil(num)
        // Add the square of the rounded number to the sum
        sum += int(math.Pow(float64(rounded), 2))
    }
    return sum
}

func main() {
    lst := []float64{1, 2, 3}
    fmt.Println(SumSquares(lst)) // Output: 14
}
```
This solution uses the `math.Ceil` function to round each number in the list to the upper int, and then calculates the sum of the squares of these rounded numbers using a loop and the `math.Pow` function. The result is returned as an integer. The `main` function demonstrates how to use this solution with a sample list of numbers.