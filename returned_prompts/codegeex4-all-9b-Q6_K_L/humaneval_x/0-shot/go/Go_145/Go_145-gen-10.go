```go
func OrderByPoints(nums []int) []int {
    sorted := make([]int, len(nums))
    copy(sorted, nums)
    sort.Slice(sorted, func(i, j int) bool {
        sumI := 0
        sumJ := 0
        for _, num := range strconv.Itoa(sorted[i]) {
            sumI += int(num - '0')
        }
        for _, num := range strconv.Itoa(sorted[j]) {
            sumJ += int(num - '0')
        }
        if sumI == sumJ {
            return i < j
        }
        return sumI < sumJ
    })
    return sorted
}
```