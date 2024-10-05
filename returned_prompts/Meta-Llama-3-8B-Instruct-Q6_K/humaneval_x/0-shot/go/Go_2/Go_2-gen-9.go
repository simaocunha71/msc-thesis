Here is a simple function that truncates the decimal part of a given floating point number. It uses the built-in `math.Mod` function to calculate the remainder of the division of the number by 1, which gives us the decimal part.

```go
import (
    "math"
)

func TruncateNumber(number float64) float64 {
    return math.Mod(number, 1)
}
```

This function works because the remainder of the division of a number by 1 is equal to the decimal part of the number. For example, the decimal part of 3.5 is 0.5, and `math.Mod(3.5, 1)` returns 0.5. Similarly, the decimal part of 4.25 is 0.25, and `math.Mod(4.25, 1)` returns 0.25. This function works for any positive floating point number. 

For example, `TruncateNumber(3.5)` returns `0.5`, `TruncateNumber(4.25)` returns `0.25`, and `TruncateNumber(2.75)` returns `0.75`. 

This function assumes that the input number is a positive floating point number. If the input number is not positive, the function may not return the expected result. If you want to handle negative numbers as well, you can add a simple check at the beginning of the function. For example:

```go
func TruncateNumber(number float64) float64 {
    if number < 0 {
        return -math.Mod(-number, 1)
    }
    return math.Mod(number, 1)
}
``` 

This version of the function returns the negative of the decimal part if the input number is negative. For example, `TruncateNumber(-3.5)` returns `-0.5`, `TruncateNumber(-4.25)` returns `-0.25`, and `TruncateNumber(-2.75)` returns `-0.75`. 

This function is a simple and efficient way to truncate the decimal part of a floating point number. It is suitable for most applications where you need to truncate a floating point number. However, if you need to truncate the decimal part of a floating point number to a specific number of decimal places, you may need to use a different approach. 

For example, to truncate the decimal part of a floating point number to 2 decimal places, you can use the following function:

```go
func TruncateNumber(number float