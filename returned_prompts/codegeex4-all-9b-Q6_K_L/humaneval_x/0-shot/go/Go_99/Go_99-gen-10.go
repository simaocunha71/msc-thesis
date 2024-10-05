```go
func ClosestInteger(value string) int {
    f, _ := strconv.ParseFloat(value, 64)
    i := int(math.Round(f))
    if f-i >= 0.5 {
        return i + 1
    }
    return i
}
```
