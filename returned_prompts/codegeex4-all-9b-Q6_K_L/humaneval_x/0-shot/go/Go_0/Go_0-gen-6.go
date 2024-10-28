Here's the Go implementation for the problem:

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

In this code, we iterate through all pairs of numbers in the input slice. For each pair, we calculate the absolute difference between the two numbers. If this difference is less than the threshold, we return true to indicate that we've found two numbers closer than the threshold. If we've checked all pairs and haven't found any such pair, we return false.