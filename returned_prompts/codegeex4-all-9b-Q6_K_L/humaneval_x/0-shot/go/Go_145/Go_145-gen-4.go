```go
func OrderByPoints(nums []int) []int {
    // Use sort.Slice to sort the slice based on the sum of digits
    sort.Slice(nums, func(i, j int) bool {
        sumi := sumDigits(nums[i])
        sumj := sumDigits(nums[j])
        if sumi == sumj {
            return i < j
        }
        return sumi < sumj
    })
    return nums
}

// Helper function to calculate the sum of digits of a number
func sumDigits(n int) int {
    absN := int(math.Abs(float64(n)))
    sum := 0
    for absN != 0 {
        sum += absN % 10
        absN /= 10
    }
    return sum
}
```