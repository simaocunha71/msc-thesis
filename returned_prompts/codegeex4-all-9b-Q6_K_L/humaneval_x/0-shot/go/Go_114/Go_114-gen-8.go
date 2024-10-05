```go
func Minsubarraysum(nums []int) int {
    minSum := math.MaxInt32
    currentSum := 0
    for _, num := range nums {
        if currentSum < 0 {
            currentSum = 0
        }
        currentSum += num
        if currentSum < minSum {
            minSum = currentSum
        }
    }
    return minSum
}
```