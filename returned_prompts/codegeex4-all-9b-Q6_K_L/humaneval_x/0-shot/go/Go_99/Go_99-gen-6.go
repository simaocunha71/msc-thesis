```go
func ClosestInteger(value string) int {
    fl, _ := strconv.ParseFloat(strings.Trim(value, " "), 64)
    if fl < 0 {
        return int(math.Ceil(fl - 0.5))
    } else {
        return int(math.Floor(fl + 0.5))
    }
}
```
