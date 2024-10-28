Here is the solution in Go:

```go
func TruncateNumber(number float64) float64 {
    return number - math.Trunc(number)
}
```

Explanation:
The `math.Trunc()` function in Go returns the integer value of a number by truncating any fractional digits. Subtracting this integer value from the original number gives the decimal part.