```go
package main

import (
    "fmt"
    "sort"
)

func RescaleToUnit(numbers []float64) []float64 {
    // Sort the numbers in ascending order
    sortedNumbers := make([]float64, len(numbers))
    copy(sortedNumbers, numbers)
    sort.Float64s(sortedNumbers)

    // Calculate the range of the numbers
    min := sortedNumbers[0]
    max := sortedNumbers[len(sortedNumbers)-1]
    rangeNum := max - min

    // Apply the linear transform
    result := make([]float64, len(numbers))
    for i, num := range numbers {
        result[i] = (num - min) / rangeNum
    }

    return result
}

func main() {
    numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
    result := RescaleToUnit(numbers)
    fmt.Println(result)  // Output: [0 0.25 0.5 0.75 1]
}
```

The solution uses a simple linear transform to map the input numbers to the range [0, 1]. It first sorts the input numbers in ascending order, then calculates the range of the numbers. Then, for each number in the input list, it calculates its corresponding value in the range [0, 1] by subtracting the minimum value and dividing by the range. The result is a list of numbers where the smallest number is 0 and the largest is 1. The solution uses the `sort` package from the Go standard library to sort the numbers and the `copy` function to copy the input list to a new list for sorting. The `main` function demonstrates how to use the `RescaleToUnit` function to rescale the list [1.0, 2.0, 3.0, 4.0, 5.0]. The output is [0, 0.25, 0.5, 0.75, 1], which is the desired result.