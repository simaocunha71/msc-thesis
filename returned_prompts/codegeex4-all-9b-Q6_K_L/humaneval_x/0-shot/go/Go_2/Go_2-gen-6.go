Here's the solution for your problem:

```go
func TruncateNumber(number float64) float64 {
    return number - math.Floor(number)
}
```

In this function, `math.Floor(number)` is used to get the largest integer smaller than the given number. By subtracting this integer from the original number, we get the decimal part.