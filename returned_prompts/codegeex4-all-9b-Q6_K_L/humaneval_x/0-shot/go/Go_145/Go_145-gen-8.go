```go
func OrderByPoints(nums []int) []int {
    if len(nums) == 0 {
        return nums
    }
    var sums = make([]int, len(nums))
    for i, num := range nums {
        sums[i] = sumDigits(num)
    }
    sort.Slice(nums, func(i, j int) bool {
        if sums[i] == sums[j] {
            return i < j
        }
        return sums[i] < sums[j]
    })
    return nums
}

func sumDigits(num int) int {
    var sum int
    if num < 0 {
        sum += 1 // add 1 for negative sign
        num = -num
    }
    for num != 0 {
        sum += num % 10
        num /= 10
    }
    return sum
}
```

Please review the solution and provide feedback.