
To solve this problem, you can follow these steps:

1. Find the minimum and maximum values in the given list of numbers.
2. Calculate the difference between the maximum and minimum values.
3. Subtract the minimum value from each number in the list.
4. Divide the result by the calculated difference.

Here's an example implementation in Go:

```go
package main

import "fmt"

func RescaleToUnit(numbers []float64) []float64 {
    min := findMin(numbers)
    max := findMax(numbers)
    difference := max - min

    rescaledNumbers := make([]float64, len(numbers))
    for i, num := range numbers {
        rescaledNumbers[i] = (num - min) / difference
    }

    return rescaledNumbers
}

func findMin(numbers []float64) float64 {
    min := numbers[0]
    for _, num := range numbers {
        if num < min {
            min = num
        }
    }
    return min
}

func findMax(numbers []float64) float64 {
    max := numbers[0]
    for _, num := range numbers {
        if num > max {
            max = num
        }
    }
    return max
}

func main() {
    numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
    rescaledNumbers := RescaleToUnit(numbers)
    fmt.Println(rescaledNumbers)
}
```

This code defines a `RescaleToUnit` function that takes a slice of numbers as input and returns a slice of rescaled numbers. The `findMin` and `findMax` functions are helper functions to find the minimum and maximum values in the list, respectively.

The `RescaleToUnit` function first finds the minimum and maximum values in the input list. Then, it calculates the difference between the maximum and minimum values. Next, it creates a new slice of rescaled numbers with the same length as the input list.