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
    integerPart := math.Trunc(number)
    decimalPart := number - integerPart
    return decimalPart
}
```

This function uses Go's built-in `math.Trunc` function to truncate the decimal part of the number to 0, then subtracts the integer part from the original number to get the decimal part. 

For example, `TruncateNumber(3.5)` returns `0.5`, which is the decimal part of `3.5`. 

The function works for any positive floating point number, and always returns a decimal part that is less than 1. 

Note that `math.Trunc` rounds towards 0, so it effectively truncates the decimal part. For example, `TruncateNumber(3.9)` returns `0.9`, not `0.8`. If you want to round the decimal part instead of truncating it, you can use `math.Round` instead. 

Also, this function assumes that the input number is positive. If you want to handle negative numbers as well, you can add a check for the sign of the input number and return the absolute value of the result. 

Finally, this function does not handle the case where the input number is NaN (Not a Number) or infinity. If you want to handle these cases, you can add checks for them and return a special value, such as an error message or a sentinel value, to indicate that the input was invalid. 