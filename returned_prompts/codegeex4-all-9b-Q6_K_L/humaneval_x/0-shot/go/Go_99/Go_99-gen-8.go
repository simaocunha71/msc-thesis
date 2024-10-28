```go
func ClosestInteger(value string) int {
    num, _ := strconv.ParseFloat(value, 64)
    return int(math.Round(num))
}
```
