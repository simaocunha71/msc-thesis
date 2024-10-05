Here is a Go function that implements the `ClosestInteger` function as described:
```go
import (
    "math"
    "strconv"
    "strings"
)

func ClosestInteger(value string) int {
    num, err := strconv.ParseFloat(value, 64)
    if err != nil {
        panic(err)
    }
    return int(math.Round(float64(num)))
}
```
Here's an explanation of the code:

1. We use the `strconv.ParseFloat` function to convert the input string to a `float64` value. This function returns an error if the conversion fails, so we check for an error and panic if one occurs.
2. We use the `math.Round` function to round the `float64` value to the nearest integer. This function rounds towards the nearest even integer, which is what we want for this problem.
3. We convert the rounded `float64` value to an `int` using a type conversion. This gives us the final result.

You can test this function with the examples provided in the problem statement to see that it produces the correct results. For example:
```go
fmt.Println(ClosestInteger("10"))  // Output: 10
fmt.Println(ClosestInteger("15.3"))  // Output: 15
fmt.Println(ClosestInteger("14.5"))  // Output: 15
fmt.Println(ClosestInteger("-14.5"))  // Output: -15
```