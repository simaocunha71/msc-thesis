Here is a simple implementation in Go:

```go
import (
    "math"
)

func TruncateNumber(number float64) float64 {
    return math.Mod(number, 1)
}
```

In this implementation, we use the `math.Mod` function to get the remainder of the division of the number by 1. This remainder is the decimal part of the number. 

For example, if the input is 3.5, `math.Mod(3.5, 1)` will return 0.5, which is the decimal part of the number. 

This function works for any positive floating point number. 

For example, if the input is 2.718, `math.Mod(2.718, 1)` will return 0.718, which is the decimal part of the number. 

If the input is 1.0, `math.Mod(1.0, 1)` will return 0.0, which is the decimal part of the number. 

This function will work correctly for any positive floating point number. 

The time complexity of this function is O(1) because it does a constant amount of work. The space complexity is also O(1) because it only uses a constant amount of space. 