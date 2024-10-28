Here is the solution:

```go
import (
    "math"
)

// Given a positive floating point number, it can be decomposed into
// and integer part (largest integer smaller than given number) and decimals
// (leftover part always smaller than 1).
// 
// Return the decimal part of the number.
// >>> TruncateNumber(3.5)
// 0.5
func TruncateNumber(number float64) float64 {
    // Convert the float64 to an integer and subtract it from the float64
    // This will give us the decimal part
    decimal := number - math.Trunc(number)
    return decimal
}
```


In this function, we use the `math.Trunc` function to truncate the decimal part of the number and subtract it from the original number. This will give us the decimal part of the number. The `math.Trunc` function returns the largest integer smaller than or equal to the given number, which is exactly what we need for the integer part. The decimal part is then calculated by subtracting the integer part from the original number. This function will work correctly for any positive floating point number.