```go
func TruncateNumber(number float64) float64 {
    integer := math.Floor(number)
    return number - integer
}
```