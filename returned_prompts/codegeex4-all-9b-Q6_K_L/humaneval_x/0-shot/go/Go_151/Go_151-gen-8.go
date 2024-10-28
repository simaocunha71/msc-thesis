```go
func DoubleTheDifference(lst []float64) int {
    sum := 0
    for _, num := range lst {
        if num >= 0 && num == math.Trunc(num) && num%2 != 0 {
            sum += int(num * num)
        }
    }
    return sum
}
```