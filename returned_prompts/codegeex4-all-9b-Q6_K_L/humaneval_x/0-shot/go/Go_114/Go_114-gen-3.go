```go
func Minsubarraysum(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    minSum := nums[0]
    currentSum := nums[0]
    for i := 1; i < len(nums); i++ {
        if currentSum + nums[i] < nums[i] {
            currentSum = nums[i]
        } else {
            currentSum += nums[i]
        }
        if currentSum < minSum {
            minSum = currentSum
        }
    }
    return minSum
}
```
