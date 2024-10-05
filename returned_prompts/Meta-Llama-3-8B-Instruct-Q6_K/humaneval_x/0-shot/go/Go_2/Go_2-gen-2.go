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
    // Convert the number to an integer and float64
    intPart := math.Trunc(number)
    // Calculate the decimal part by subtracting the integer part from the number
    decimalPart := number - float64(intPart)
    return decimalPart
}
```
This function uses the `math.Trunc` function to convert the number to an integer, effectively truncating the decimal part. It then calculates the decimal part by subtracting the integer part from the original number. The result is the decimal part of the number. For example, if the input is 3.5, the function will return 0.5.