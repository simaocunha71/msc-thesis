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

func sumDigits(num int) int {
    sum := 0
    for num != 0 {
        sum += abs(num % 10)
        num /= 10
    }
    return sum
}

func abs(num int) int {
    if num < 0 {
        return -num
    }
    return num
}
```

I have added the helper functions `sumDigits` and `abs` to calculate the sum of digits and handle the absolute value of a number, respectively. The main function `OrderByPoints` uses the `sort.Slice` function to sort the slice of integers based on the sum of their digits. If two numbers have the same sum, their original order is preserved.