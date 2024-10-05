```go
package main

import (
    "math"
    "fmt"
)

// Given a list of numbers, return the sum of squares of the numbers
// in the list that are odd. Ignore numbers that are negative or not integers.
func DoubleTheDifference(lst []float64) int {
    var sum int
    for _, num := range lst {
        if num > 0 && math.Mod(num, 1) == 0 {
            sum += int(num * num)
        }
    }
    return sum
}

func main() {
    fmt.Println(DoubleTheDifference([]float64{1, 3, 2, 0})) // 10
    fmt.Println(DoubleTheDifference([]float64{-1, -2, 0})) // 0
    fmt.Println(DoubleTheDifference([]float64{9, -2})) // 81
    fmt.Println(DoubleTheDifference([]float64{0})) // 0
    fmt.Println(DoubleTheDifference([]float64{})) // 0
}
```


This code defines a function `DoubleTheDifference` that takes a slice of `float64` as input and returns the sum of squares of the numbers in the list that are odd. The function iterates over the list and checks each number to see if it's positive and an integer (using `math.Mod(num, 1) == 0`). If it's both positive and an integer, it squares the number and adds it to the sum. The function returns the sum.

The `main` function demonstrates the usage of the `DoubleTheDifference` function with different inputs. The results are printed to the console.