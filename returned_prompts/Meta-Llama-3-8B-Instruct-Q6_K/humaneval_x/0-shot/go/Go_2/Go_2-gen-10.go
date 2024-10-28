Here is a simple and efficient solution in Go:
```go
import (
    "math"
)

func TruncateNumber(number float64) float64 {
    return number - math.Trunc(number)
}
```
Explanation:

* `math.Trunc` returns the integer part of the number, which is the largest integer smaller than the given number.
* We subtract the integer part from the original number to get the decimal part.

For example, if the input is 3.5, `math.Trunc(3.5)` returns 3.0, and 3.5 - 3.0 = 0.5, which is the correct decimal part.

This solution works for all positive floating point numbers, and it is efficient because it only requires a single operation to truncate the number.