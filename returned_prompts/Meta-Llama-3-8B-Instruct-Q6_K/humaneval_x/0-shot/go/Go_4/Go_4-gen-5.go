Here is a simple Go function that calculates the Mean Absolute Deviation (MAD) of a given list of input numbers:

```go
package main

import (
    "fmt"
    "math"
)

// For a given list of input numbers, calculate Mean Absolute Deviation
// around the mean of this dataset.
// Mean Absolute Deviation is the average absolute difference between each
// element and a centerpoint (mean in this case):
// MAD = average | x - x_mean |
// >>> MeanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])
// 1.0
func MeanAbsoluteDeviation(numbers []float64) float64 {
    // Calculate the mean of the input numbers
    mean := math.NaN()
    sum := 0.0
    for _, num := range numbers {
        sum += num
    }
    mean = sum / float64(len(numbers))

    // Calculate the absolute deviations from the mean
    var deviations []float64
    for _, num := range numbers {
        deviations = append(deviations, math.Abs(num-mean))
    }

    // Calculate the mean of the absolute deviations
    mad := 0.0
    for _, dev := range deviations {
        mad += dev
    }
    mad /= float64(len(deviations))

    return mad
}

func main() {
    numbers := []float64{1.0, 2.0, 3.0, 4.0}
    fmt.Println(MeanAbsoluteDeviation(numbers))  // Output: 1
}
```

This function first calculates the mean of the input numbers. Then it calculates the absolute deviations from the mean, and finally calculates the mean of these absolute deviations. The result is the Mean Absolute Deviation. In the `main` function, we test this function with an example input. The output should be 1.0.