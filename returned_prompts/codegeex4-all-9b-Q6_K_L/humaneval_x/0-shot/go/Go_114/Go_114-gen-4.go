```go
func Minsubarraysum(nums []int) int {
    min_sum := math.MaxInt32
    current_sum := 0
    for _, num := range nums {
        current_sum = 0
        for _, n := range nums {
            current_sum += n
            if current_sum < min_sum {
                min_sum = current_sum
            }
        }
    }
    return min_sum
}
```
