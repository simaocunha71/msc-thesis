```go
func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    var sign int = 1
    var sum int = 0
    for _, v := range arr {
        if v == 0 {
            return 0
        }
        if v < 0 {
            sign *= -1
        }
        sum += int(math.Abs(float64(v)))
    }
    return sign * sum
}
```