```go
func Minsubarraysum(nums []int) int {
    sum := nums[0]
    min := nums[0]
    for i := 1; i < len(nums); i++ {
        sum = math.Min(float64(nums[i]), float64(sum)+float64(nums[i]))
        if sum < min {
            min = sum
        }
    }
    return min
}
```