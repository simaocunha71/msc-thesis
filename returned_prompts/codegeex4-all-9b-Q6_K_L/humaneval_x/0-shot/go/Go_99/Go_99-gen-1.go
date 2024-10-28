```go
func ClosestInteger(value string) int {
    var number float64
    var err error
    if strings.Contains(value, ".") {
        number, err = strconv.ParseFloat(value, 64)
        if err != nil {
            return -1
        }
    } else {
        number, err = strconv.Atoi(value)
        if err != nil {
            return -1
        }
    }
    if math.Mod(number, 1) >= 0.5 {
        number = math.Ceil(number)
    } else {
        number = math.Floor(number)
    }
    return int(number)
}
```
