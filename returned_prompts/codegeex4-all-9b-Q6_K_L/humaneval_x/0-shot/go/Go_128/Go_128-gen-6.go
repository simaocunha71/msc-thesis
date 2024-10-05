```go
func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }

    prod := 1
    sum := 0
    for _, num := range arr {
        if num == 0 {
            return 0
        }
        if num < 0 {
            prod *= -1
        }
        sum += int(math.Abs(float64(num)))
    }
    return prod * sum
}
```
