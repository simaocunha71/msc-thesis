Here is a simple function in Go that truncates a floating point number to its decimal part:

```go
import (
    "math"
)

func TruncateNumber(number float64) float64 {
    return number - math.Trunc(number)
}
```

In this function, `math.Trunc` is used to truncate the number to its integer part. Then the result is subtracted from the original number to get its decimal part. This works because the decimal part is always the difference between the original number and its integer part. 

For example, `TruncateNumber(3.5)` will return `0.5`, which is the decimal part of `3.5`. 

Note: This function assumes that the input number is positive. If the input number can be negative, you might want to consider handling that case separately. 

Also, the result of this function will be a float64, even if the decimal part is a repeating decimal. If you want to get a string representation of the decimal part, you can use the `fmt.Sprintf` function to convert the result to a string. For example: `fmt.Sprintf("%.1f", TruncateNumber(3.5))` will return the string `"0.5"`. 

Here is how you can test this function:

```go
func main() {
    fmt.Println(TruncateNumber(3.5))  // prints 0.5
    fmt.Println(TruncateNumber(1.0))  // prints 0.0
    fmt.Println(TruncateNumber(2.718))  // prints 0.718
}
``` 