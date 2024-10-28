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
    mean := calculateMean(numbers)
    var sum float64
    for _, num := range numbers {
        sum += math.Abs(num - mean)
    }
    return sum / float64(len(numbers))
}

func calculateMean(numbers []float64) float64 {
    var sum float64
    for _, num := range numbers {
        sum += num
    }
    return sum / float64(len(numbers))
}
```
Explanation:
1. The `calculateMean` function calculates the mean of the input numbers.
2. The `MeanAbsoluteDeviation` function calculates the mean absolute deviation by iterating over each number in the input list, subtracting the mean from each number, taking the absolute value of the difference, and summing these values. The mean absolute deviation is then calculated as the average of these values.
3. The result is the mean absolute deviation around the mean of the input dataset. 

You can test this function with a list of numbers, for example:
```go
numbers := []float64{1.0, 2.0, 3.0, 4.0}
result := MeanAbsoluteDeviation(numbers)
fmt.Println(result) // Output: 1.0
```  