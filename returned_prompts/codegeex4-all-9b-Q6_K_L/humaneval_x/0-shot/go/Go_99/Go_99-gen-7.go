```go
func ClosestInteger(value string) int {
    var x float64 = 0
    if strings.Contains(value, ".") {
        x, _ = strconv.ParseFloat(value, 64)
    } else {
        i, _ := strconv.Atoi(value)
        x = float64(i)
    }
    return int(math.Round(x))
}
```
