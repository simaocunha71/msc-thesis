    // Sort by the sum of digits
    sort.Slice(nums, func(i, j int) bool {
        return sumDigits(nums[i]) < sumDigits(nums[j])
    })
    // Sort by the original index
    sort.Slice(nums, func(i, j int) bool {
        return sumDigits(nums[i]) == sumDigits(nums[j]) && i < j
    })
    return nums
}

func sumDigits(num int) int {
    return sumDigitsPositive(int(math.Abs(float64(num))))
}

func sumDigitsPositive(num int) int {
    if num < 10 {
        return num
    }
    return num%10 + sumDigitsPositive(num/10)
}

