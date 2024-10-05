Here is a Go function that meets the requirements:
```go
import (
    "math"
)

func DoubleTheDifference(lst []float64) int {
    var sum int
    for _, num := range lst {
        if num >= 0 && math.Mod(num, 1) == 0 {
            sum += int(num * num)
        }
    }
    return sum
}
```
This function iterates over the input list, and for each number, it checks if it's non-negative and an integer (i.e., `math.Mod(num, 1) == 0`). If it is, it adds the square of the number to the sum. Finally, it returns the sum.

Note that we use `int(num * num)` to convert the square of the number to an integer, since the square of a float64 may not be exactly representable as an integer. This is safe because we only add the result to the sum, and the sum is an integer. If the input list is empty, the function will simply return 0, as required.