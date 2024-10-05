Here is the solution in Go:

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
    // Calculate the mean
    mean := math.NaN()
    for _, num := range numbers {
        if math.IsNaN(mean) {
            mean = num
        } else {
            mean += num
        }
    }
    mean /= float64(len(numbers))
    
    // Calculate the Mean Absolute Deviation
    var mad float64
    for _, num := range numbers {
        mad += math.Abs(num - mean)
    }
    mad /= float64(len(numbers))
    
    return mad
}
```

This function first calculates the mean of the input numbers. It then calculates the Mean Absolute Deviation by summing the absolute differences between each number and the mean, and dividing by the number of elements in the input list. The `math.Abs` function is used to calculate the absolute value of the differences. The result is returned as a float64 value.