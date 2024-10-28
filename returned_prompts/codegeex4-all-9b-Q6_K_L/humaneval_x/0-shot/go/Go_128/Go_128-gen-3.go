```go
func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    prodSign := 1
    sum := 0
    for _, num := range arr {
        if num < 0 {
            prodSign *= -1
        } else if num == 0 {
            prodSign = 0
        }
        sum += int(math.Abs(float64(num)))
    }
    return prodSign * sum
}
```