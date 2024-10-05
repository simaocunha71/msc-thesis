    sort.Slice(nums, func(i, j int) bool {
        sum1 := 0
        for _, digit := range strconv.Itoa(nums[i]) {
            sum1 += int(digit - '0')
        }
        sum2 := 0
        for _, digit := range strconv.Itoa(nums[j]) {
            sum2 += int(digit - '0')
        }
        return sum1 < sum2
    })
    return nums
}



