Here is the solution:

```go
package main

import (
    "math"
    "fmt"
)

func SumSquares(lst []float64) int {
    var sum int
    for _, num := range lst {
        // Round each element to the upper int(Ceiling)
        rounded := math.Ceil(num)
        // Convert the rounded number to int
        roundedInt := int(rounded)
        // Square the rounded int
        square := roundedInt * roundedInt
        // Add the square to the sum
        sum += square
    }
    return sum
}

func main() {
    fmt.Println(SumSquares([]float64{1, 2, 3})) // Output: 14
    fmt.Println(SumSquares([]float64{1, 4, 9})) // Output: 98
    fmt.Println(SumSquares([]float64{1, 3, 5, 7})) // Output: 84
    fmt.Println(SumSquares([]float64{1.4, 4.2, 0})) // Output: 29
    fmt.Println(SumSquares([]float64{-2.4, 1, 1})) // Output: 6
}
```


The `SumSquares` function iterates over the input list of floats, rounds each number to the upper int using `math.Ceil`, converts the rounded float to an int, squares the int, and adds the square to the sum. Finally, the function returns the sum. The `main` function tests the `SumSquares` function with different inputs and prints the results.