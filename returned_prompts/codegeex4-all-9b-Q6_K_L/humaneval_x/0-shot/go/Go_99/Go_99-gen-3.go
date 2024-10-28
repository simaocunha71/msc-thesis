```go
func ClosestInteger(value string) int {
    var result float64
    if strings.Contains(value, ".") {
        temp, _ := strconv.ParseFloat(value, 64)
        result = math.Round(temp)
    } else {
        temp, _ := strconv.Atoi(value)
        result = float64(temp)
    }
    return int(result)
}
```
