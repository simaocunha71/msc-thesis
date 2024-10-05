```go
func ClosestInteger(value string) int {
    var result float64
    value = strings.Replace(value, ",", ".", -1)

    if strings.Contains(value, ".") {
        result, _ = strconv.ParseFloat(value, 64)
        if result < 0 {
            if result - math.Floor(result) < -0.5 {
                return int(math.Floor(result))
            } else {
                return int(math.Ceil(result))
            }
        } else {
            if result - math.Floor(result) < 0.5 {
                return int(math.Floor(result))
            } else {
                return int(math.Ceil(result))
            }
        }
    } else {
        result, _ = strconv.Atoi(value)
    }

    return int(result)
}
```