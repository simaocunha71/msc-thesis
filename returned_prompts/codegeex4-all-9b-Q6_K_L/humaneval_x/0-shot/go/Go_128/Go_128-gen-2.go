```go
func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    var sum int
    var prodSign int
    for _, num := range arr {
        sum += int(math.Abs(float64(num)))
        if num < 0 {
            prodSign *= -1
        } else if num == 0 {
            prodSign = 0
        }
    }
    return sum * prodSign
}
```
