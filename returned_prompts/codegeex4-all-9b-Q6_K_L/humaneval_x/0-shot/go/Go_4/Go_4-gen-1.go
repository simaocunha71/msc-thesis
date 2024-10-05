To calculate the Mean Absolute Deviation (MAD) of a list of numbers, you can follow these steps:

1. Compute the mean (average) of the list of numbers.
2. For each number in the list, calculate the absolute difference between the number and the mean.
3. Sum these absolute differences.
4. Divide the sum by the number of elements in the list (to get the average).

Here's the Go code that implements these steps:

```go
import (
    "math"
)

// MeanAbsoluteDeviation calculates the Mean Absolute Deviation (MAD) of a list of numbers.
func MeanAbsoluteDeviation(numbers []float64) float64 {
    // Step 1: Calculate the mean of the numbers
    mean := mean(numbers)

    // Step 2 & 3: Calculate the sum of the absolute differences from the mean
    sum := 0.0
    for _, number := range numbers {
        sum += math.Abs(number - mean)
    }

    // Step 4: Divide by the number of elements to get the average
    return sum / float64(len(numbers))
}

// mean calculates the mean of a list of numbers.
func mean(numbers []float64) float64 {
    var total float64
    for _, number := range numbers {
        total += number
    }
    return total / float64(len(numbers))
}
```

This code defines a `MeanAbsoluteDeviation` function that first calculates the mean of the input numbers using a helper function `mean`. Then, it calculates the sum of the absolute differences between each number and the mean. Finally, it divides this sum by the number of elements in the list to get the average, which is the Mean Absolute Deviation.