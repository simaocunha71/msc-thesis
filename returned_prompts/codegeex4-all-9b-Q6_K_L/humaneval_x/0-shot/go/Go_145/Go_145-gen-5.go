```go
func OrderByPoints(nums []int) []int {
    return sort.Slice(nums, func(i, j int) bool {
        sumI := sumDigits(nums[i])
        sumJ := sumDigits(nums[j])
        if sumI != sumJ {
            return sumI < sumJ
        }
        return i < j
    })
}

func sumDigits(n int) int {
    sum := 0
    absN := abs(n)
    for absN > 0 {
        sum += absN % 10
        absN /= 10
    }
    return sum
}

func abs(n int) int {
    if n < 0 {
        return -n
    }
    return n
}
```