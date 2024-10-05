```go
func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }

    var prod int
    var sum int
    for _, v := range arr {
        if v < 0 {
            prod *= -1
        } else if v == 0 {
            prod = 0
            break
        } else {
            prod *= 1
        }
        sum += int(math.Abs(float64(v)))
    }
    return prod * sum
}
```