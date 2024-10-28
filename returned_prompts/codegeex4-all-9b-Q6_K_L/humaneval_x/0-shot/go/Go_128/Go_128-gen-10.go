```go
func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    product := 1
    sign := 1
    for _, num := range arr {
        if num == 0 {
            return 0
        }
        if num < 0 {
            sign *= -1
        }
        product *= abs(num)
    }
    return sign * product
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```
