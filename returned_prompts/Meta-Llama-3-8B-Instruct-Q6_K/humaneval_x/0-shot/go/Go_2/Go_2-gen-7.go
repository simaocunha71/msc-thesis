Here is a simple and efficient solution:
```go
func TruncateNumber(number float64) float64 {
    intPart := math.Trunc(number)
    return number - float64(intPart)
}
```
This function uses the `math.Trunc` function to truncate the integer part of the number, and then subtracts the integer part from the original number to get the decimal part. This approach is simple and efficient, as it avoids the need to use string manipulation or complex arithmetic operations.