    sort.Slice(nums, func(i, j int) bool {
        sumI := 0
        sumJ := 0
        for _, r := range strconv.Itoa(nums[i]) {
            sumI += int(r - '0')
        }
        for _, r := range strconv.Itoa(nums[j]) {
            sumJ += int(r - '0')
        }
        if sumI == sumJ {
            return nums[i] < nums[j]
        }
        return sumI < sumJ
    })
    return nums
}



