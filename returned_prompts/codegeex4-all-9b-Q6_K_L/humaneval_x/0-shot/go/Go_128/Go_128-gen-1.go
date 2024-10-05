```go
func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    prod := 1
    sum := 0
    for _, x := range arr {
        sum += int(math.Abs(float64(x)))
        prod *= sign(x)
    }
    return prod * sum
}

func sign(x int) int {
    if x < 0 {
        return -1
    }
    if x > 0 {
        return 1
    }
    return 0
}
```