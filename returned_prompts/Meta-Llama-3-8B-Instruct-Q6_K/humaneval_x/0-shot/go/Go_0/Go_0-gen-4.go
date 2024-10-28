Here is the implementation in Go:
```go
import (
    "math"
)

func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i]-numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}
```
Explanation:

The function `HasCloseElements` takes two arguments: `numbers` which is a slice of floating point numbers and `threshold` which is a floating point number.

It iterates over the `numbers` slice using two nested loops. The outer loop iterates over each element in the slice, and the inner loop iterates over each element that comes after the current element in the outer loop.

For each pair of elements, it calculates the absolute difference between them using the `math.Abs` function. If the absolute difference is less than the `threshold`, it returns `true` immediately, indicating that it has found two elements that are closer to each other than the threshold.

If the function iterates over the entire slice without finding two elements that are closer to each other than the threshold, it returns `false`. This means that no two elements are closer to each other than the threshold.