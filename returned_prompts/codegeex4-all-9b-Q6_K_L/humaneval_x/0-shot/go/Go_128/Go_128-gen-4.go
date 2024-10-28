```go
func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    prod := 1
    sum := 0
    for _, i := range arr {
        if i == 0 {
            return 0
        }
        if i < 0 {
            prod *= -1
        }
        sum += int(math.Abs(float64(i)))
    }
    return prod * sum
}
```