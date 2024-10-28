```go
func ClosestInteger(value string) int {
    v, _ := strconv.ParseFloat(strings.Replace(value, ",", ".", -1), 64)
    return int(math.Round(v))
}
```