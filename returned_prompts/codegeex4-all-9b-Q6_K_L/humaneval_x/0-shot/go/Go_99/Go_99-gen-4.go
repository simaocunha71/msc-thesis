```go
func ClosestInteger(value string) int {
    v, _ := strconv.ParseFloat(strings.TrimSpace(value), 64)
    if v < 0 {
        return int(math.Ceil(v - 0.5))
    } else {
        return int(math.Floor(v + 0.5))
    }
}
```
