```go
import (
    "math"
)

// For a given list of input numbers, calculate Mean Absolute Deviation
// around the mean of this dataset.
// Mean Absolute Deviation is the average absolute difference between each
// element and a centerpoint (mean in this case):
// MAD = average | x - x_mean |
func MeanAbsoluteDeviation(numbers []float64) float64 {
    sum := 0.0
    mean := 0.0
    for _, num := range numbers {
        mean += num
    }
    mean /= float64(len(numbers))
    for _, num := range numbers {
        sum += math.Abs(num - mean)
    }
    return sum / float64(len(numbers))
}
```
Explanation:

1. We iterate over the input numbers to calculate the mean.
2. We iterate over the input numbers again to calculate the sum of the absolute differences between each element and the mean.
3. We return the sum divided by the number of elements, which is the Mean Absolute Deviation.

Example usage:
```go
numbers := []float64{1.0, 2.0, 3.0, 4.0}
MAD := MeanAbsoluteDeviation(numbers)
fmt.Println(MAD)  // Output: 1.0
```
Note: The `math.Abs` function is used to calculate the absolute difference between each element and the mean. This function returns the absolute value of a number. For example, `math.Abs(-3.0)` would return `3.0`. This is used to calculate the absolute difference between each element and the mean, which is necessary for calculating the Mean Absolute Deviation.