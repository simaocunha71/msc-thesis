Here is a simple implementation in Go:

```go
import (
    "strconv"
)

func ChangeBase(x int, base int) string {
    if x < base {
        return strconv.Itoa(x)
    }
    result := ""
    for x > 0 {
        result = strconv.Itoa(x % base) + result
        x = x / base
    }
    return result
}
```

This function works by repeatedly dividing the input number `x` by the target base and prepending the remainder to the result string. This process continues until `x` is less than the base, at which point the function returns the resulting string.

The base case is when `x` is less than `base`, in which case the function simply converts `x` to a string using `strconv.Itoa`.

Note that the conversion is done in-place, i.e., the result string is built by prepending the remainder to the front of the string, rather than appending it to the end. This is because we want to maintain the correct order of the digits in the output string. If we were to append the remainder to the end of the string, the digits would be in the wrong order. For example, if the input number is 8 and the target base is 3, the correct output would be "22", not "28". By prepending the remainder to the front of the string, we ensure that the digits are in the correct order.