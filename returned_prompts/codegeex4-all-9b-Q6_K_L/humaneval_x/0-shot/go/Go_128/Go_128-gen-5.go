```go
func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    prod := 1
    sum := 0
    for _, x := range arr {
        if x < 0 {
            prod *= -1
        }
        if x != 0 {
            sum += int(math.Abs(float64(x)))
        }
    }
    return prod * sum
}
```