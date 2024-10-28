```go
package main

import (
    "fmt"
    "sort"
)

func RescaleToUnit(numbers []float64) []float64 {
    if len(numbers) < 2 {
        panic("List must have at least two elements")
    }

    // Find the minimum and maximum values
    min := numbers[0]
    max := numbers[0]
    for _, num := range numbers[1:] {
        if num < min {
            min = num
        }
        if num > max {
            max = num
        }
    }

    // Create a new slice with the rescaled values
    result := make([]float64, len(numbers))
    for i, num := range numbers {
        result[i] = (num - min) / (max - min)
    }

    return result
}

func main() {
    numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
    fmt.Println(RescaleToUnit(numbers))
}
```

Explanation:
The function RescaleToUnit takes a slice of float64 numbers as input and returns a new slice with the same numbers, but rescaled to have a minimum value of 0 and a maximum value of 1.

First, it finds the minimum and maximum values in the input slice. Then, it creates a new slice and iterates over the input slice, subtracting the minimum value from each number and dividing the result by the range of the input slice (i.e., the difference between the maximum and minimum values). This rescales each number to be between 0 and 1.

In the main function, we create a slice of numbers and call the RescaleToUnit function with that slice as input. The resulting slice is then printed to the console.

Note that this function assumes that the input slice has at least two elements. If the input slice has only one element, or is empty, the function will panic with an error message. You may want to add additional error handling or input validation depending on your specific use case.