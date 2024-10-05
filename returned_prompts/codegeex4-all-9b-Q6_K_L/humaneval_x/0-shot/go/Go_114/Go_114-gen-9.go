```go
func Minsubarraysum(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    
    minSum := math.MaxInt32
    currentSum := 0
    
    for _, num := range nums {
        currentSum += num
        if currentSum < minSum {
            minSum = currentSum
        }
        if currentSum > 0 {
            currentSum = 0
        }
    }
    
    return minSum
}
```