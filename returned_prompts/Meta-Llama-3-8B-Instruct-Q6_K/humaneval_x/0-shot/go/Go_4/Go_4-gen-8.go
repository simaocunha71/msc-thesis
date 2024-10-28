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
    sum := 0.0
    for _, num := range numbers {
        sum += num
    }
    return sum / float64(len(numbers))
}
```
Explanation:

1. We define a function `MeanAbsoluteDeviation` that takes a slice of floating point numbers as input.
2. We calculate the mean of the input numbers using the `calculateMean` function.
3. We iterate over the input numbers, calculate the absolute difference between each number and the mean, and sum up these differences.
4. We divide the sum by the length of the input slice to get the Mean Absolute Deviation.
5. The `calculateMean` function simply calculates the mean of the input numbers by summing them up and dividing by the length of the slice. 

Note: This code assumes that the input slice is not empty. You may want to add error handling to handle the case where the input slice is empty. 

You can test this function with the example you provided:
```go
numbers := []float64{1.0, 2.0, 3.0, 4.0}
result := MeanAbsoluteDeviation(numbers)
fmt.Println(result) // Output: 1.0
``` 0
Note: This code assumes that the input slice is not empty. You may want to add error handling to handle the case where the input slice is empty. 

You can test this function with the example you provided:
```go
numbers := []float64{1.0, 2.0, 3.0, 4.0}
result := MeanAbsoluteDeviation(numbers)
fmt.Println(result) // Output: 1.0