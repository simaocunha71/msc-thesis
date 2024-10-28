```go
package main

import (
    "math"
)

func DoubleTheDifference(lst []float64) int {
    var sum int
    for _, num := range lst {
        if num > 0 && math.Mod(num, 2) == 1 { // Check if number is positive and odd
            sum += int(num * num) // Add square of the number to the sum
        }
    }
    return sum
}

func main() {
    print(DoubleTheDifference([]float64{1, 3, 2, 0})) // Output: 10
    print(DoubleTheDifference([]float64{-1, -2, 0})) // Output: 0
    print(DoubleTheDifference([]float64{9, -2})) // Output: 81
    print(DoubleTheDifference([]float64{0})) // Output: 0
    print(DoubleTheDifference([]float64{})) // Output: 0
}
```


The function `DoubleTheDifference` takes a slice of `float64` as an input and returns an integer. It initializes a variable `sum` to 0. Then, it iterates over each number in the input list. For each number, it checks if the number is positive and odd using the condition `num > 0 && math.Mod(num, 2) == 1`. If the number is positive and odd, it adds the square of the number to the `sum`. Finally, it returns the `sum`. The `main` function demonstrates the usage of the `DoubleTheDifference` function with different inputs.