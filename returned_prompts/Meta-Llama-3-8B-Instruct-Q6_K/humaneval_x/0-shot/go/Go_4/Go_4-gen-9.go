Here is the solution:
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
    mean := math.NaN()
    for _, num := range numbers {
        if math.IsNaN(mean) {
            mean = num
        } else {
            mean += num
        }
    }
    mean /= float64(len(numbers))

    // Calculate the mean absolute deviation
    var sum float64
    for _, num := range numbers {
        sum += math.Abs(num - mean)
    }
    return sum / float64(len(numbers))
}
```
This solution calculates the mean of the input numbers and then calculates the mean absolute deviation by iterating through the numbers, subtracting the mean from each number, taking the absolute value, and summing up the results. The mean absolute deviation is then calculated by dividing the sum by the number of elements in the input array.