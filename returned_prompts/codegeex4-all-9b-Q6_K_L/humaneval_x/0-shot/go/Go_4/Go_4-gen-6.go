To calculate the Mean Absolute Deviation (MAD) for a list of numbers, you first need to find the mean of the numbers. Then, for each number in the list, calculate the absolute difference between that number and the mean, and finally, find the average of these differences. Here's how you can implement this in Go:

```go
import (
    "math"
)

// MeanAbsoluteDeviation calculates the Mean Absolute Deviation of a list of numbers.
func MeanAbsoluteDeviation(numbers []float64) float64 {
    // Calculate the mean of the numbers
    mean := 0.0
    for _, number := range numbers {
        mean += number
    }
    mean /= float64(len(numbers))

    // Calculate the MAD by summing the absolute differences from the mean
    mad := 0.0
    for _, number := range numbers {
        mad += math.Abs(number - mean)
    }
    mad /= float64(len(numbers))

    return mad
}
```

This function works as follows:
1. It calculates the mean of the input numbers by summing them up and dividing by the number of elements.
2. It then iterates over the numbers, calculating the absolute difference between each number and the mean, and sums these differences.
3. Finally, it divides the sum of the absolute differences by the number of elements to get the MAD. 

You can call this function with a slice of float64 values to get the Mean Absolute Deviation. For example:

```go
numbers := []float64{1.0, 2.0, 3.0, 4.0}
fmt.Println(MeanAbsoluteDeviation(numbers)) // Output: 1.0
```

This function assumes that the input slice is not empty. If there's a possibility of an empty slice, you might want to add error handling to the function.