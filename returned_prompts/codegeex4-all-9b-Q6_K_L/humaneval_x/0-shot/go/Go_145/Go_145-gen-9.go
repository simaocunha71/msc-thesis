```go
func OrderByPoints(nums []int) []int {
    sort.Slice(nums, func(i, j int) bool {
        sumI := sumDigits(nums[i])
        sumJ := sumDigits(nums[j])
        if sumI == sumJ {
            return i < j
        }
        return sumI < sumJ
    })
    return nums
}

func sumDigits(n int) int {
    total := 0
    for n != 0 {
        total += abs(n % 10)
        n /= 10
    }
    return total
}

func abs(n int) int {
    if n < 0 {
        return -n
    }
    return n
}
```