```go
func TruncateNumber(number float64) float64 {
    integerPart := math.Trunc(number)
    return number - float64(integerPart)
}
```
Explanation:
In Go, you can use the `math.Trunc` function to truncate a floating point number to an integer. This function returns the integer part of the number, discarding the decimal part.

In this function, we first calculate the integer part of the input number using `math.Trunc`. Then, we subtract this integer part from the original number to get the decimal part. The result is the decimal part of the original number. For example, if the input number is 3.5, `math.Trunc(3.5)` returns 3, and `3.5 - 3` returns 0.5. Therefore, the output of the function is 0.5.