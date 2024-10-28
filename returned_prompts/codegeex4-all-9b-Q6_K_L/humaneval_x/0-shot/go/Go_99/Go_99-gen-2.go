```go
func ClosestInteger(value string) int {
    var num float64
    if strings.Contains(value, ".") {
        num, _ = strconv.ParseFloat(value, 64)
    } else {
        num, _ = strconv.Atoi(value)
    }
    if num >= 0 {
        return int(num + math.Copysign(0.5, num))
    }
    return int(num - math.Copysign(0.5, num))
}
```
