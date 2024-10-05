```go
func MaxFill(grid [][]int, capacity int) int {
    var sum int
    for _, v := range grid {
        for _, j := range v {
            sum += j
        }
    }
    return sum / capacity
}
```
