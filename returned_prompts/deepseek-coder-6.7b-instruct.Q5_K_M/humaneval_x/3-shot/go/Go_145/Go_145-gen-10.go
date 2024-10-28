    sort.SliceStable(nums, func(i, j int) bool {
        sumI := 0
        sumJ := 0
        for _, n := range strconv.Itoa(nums[i]) {
            sumI += int(n - '0')
        }
        for _, n := range strconv.Itoa(nums[j]) {
            sumJ += int(n - '0')
        }
        return sumI < sumJ
    })
    return nums
}



