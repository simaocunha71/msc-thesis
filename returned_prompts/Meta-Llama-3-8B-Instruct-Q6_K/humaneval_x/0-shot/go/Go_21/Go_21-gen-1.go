Here is a Go function that rescales a list of numbers to the unit interval [0, 1]:

```go
package main

import (
    "fmt"
    "math"
)

func RescaleToUnit(numbers []float64) []float64 {
    min := math.MinFloat64
    max := -math.MinFloat64
    for _, num := range numbers {
        if num > max {
            max = num
        }
        if num < min {
            min = num
        }
    }
    if min == max {
        return numbers // all numbers are equal, return the original list
    }
    scaled := make([]float64, len(numbers))
    for i, num := range numbers {
        scaled[i] = (num - min) / (max - min)
    }
    return scaled
}

func main() {
    numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
    scaled := RescaleToUnit(numbers)
    fmt.Println(scaled) // [0 0.25 0.5 0.75 1]
}
```

This function first finds the minimum and maximum values in the input list. If all numbers are equal, it returns the original list. Otherwise, it rescales each number to the unit interval by subtracting the minimum and dividing by the range. The result is a new list with the same length as the input list. The main function demonstrates how to use this function with a sample list of numbers.