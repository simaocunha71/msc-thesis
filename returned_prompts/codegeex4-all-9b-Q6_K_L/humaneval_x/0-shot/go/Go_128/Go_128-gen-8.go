```go
func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    prodSigns := 1
    sumMagnitudes := 0
    for _, num := range arr {
        if num < 0 {
            prodSigns *= -1
        } else if num == 0 {
            prodSigns = 0
        }
        sumMagnitudes += abs(num)
    }
    return prodSigns * sumMagnitudes
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```
