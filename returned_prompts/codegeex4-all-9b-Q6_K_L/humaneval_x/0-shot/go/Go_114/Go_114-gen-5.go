```go
func Minsubarraysum(nums []int) int {
    sum := nums[0]
    minSum := nums[0]
    for i := 1; i < len(nums); i++ {
        sum += nums[i]
        if nums[i] < 0 {
            sum = nums[i]
        }
        if sum < minSum {
            minSum = sum
        }
    }
    return minSum
}
```