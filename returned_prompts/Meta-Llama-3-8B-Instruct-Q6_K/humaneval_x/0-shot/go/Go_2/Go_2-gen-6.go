You can use the built-in `math.Modf` function to decompose the number into its integer and fractional parts. The `math.Modf` function returns a tuple containing the integer and fractional parts of the number.

Here is the corrected code:

```go
import (
    "math"
)

func TruncateNumber(number float64) float64 {
    var f float64
    var i float64
    var dec float64
    var result float64
    f, i = math.Modf(number)
    dec = f
    result = dec
    return result
}
```

In this function, the `math.Modf` function is used to decompose the input number into its integer and fractional parts. The fractional part is then returned as the result.

For example, if you call `TruncateNumber(3.5)`, the function will return `0.5`, which is the decimal part of the number.