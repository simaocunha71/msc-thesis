Here is a Go solution for the problem:

```go
import (
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
    // Calculate the mean of the numbers
    mean := calculateMean(numbers)

    // Calculate the absolute deviations from the mean
    deviations := make([]float64, len(numbers))
    for i, num := range numbers {
        deviations[i] = math.Abs(num - mean)
    }

    // Calculate the mean of the absolute deviations
    mad := calculateMean(deviations)

    return mad
}

// Calculate the mean of a slice of numbers
func calculateMean(numbers []float64) float64 {
    sum := 0.0
    for _, num := range numbers {
        sum += num
    }
    return sum / float64(len(numbers))
}
```
This program calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It first calculates the mean of the numbers, then calculates the absolute deviations of each number from the mean, and finally calculates the mean of these absolute deviations. The calculateMean function is a helper function that calculates the mean of a slice of numbers. The MeanAbsoluteDeviation function returns the calculated MAD. 

This program assumes that the input list of numbers is not empty. If the list is empty, it will panic when trying to calculate the mean. You might want to add a check for an empty list and return a special value (like math.NaN) or an error. 

This program uses the math.Abs function from the math package to calculate the absolute value of a number. This function returns the magnitude of its argument, which is the value without its sign. For example, math.Abs(-1.0) returns 1.0. 

The MeanAbsoluteDeviation function returns the calculated MAD as a float64 value. This value is the average absolute difference between each element in the input list and the mean of the list. The unit test `>>> MeanAbsoluteDeviation([1.0, 2.0, 3.0, 4