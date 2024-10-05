    sort.Slice(nums, func(i, j int) bool {
        sumI := 0
        sumJ := 0
        for _, r := range strconv.Itoa(nums[i]) {
            n, _ := strconv.Atoi(string(r))
            sumI += n
        }
        for _, r := range strconv.Itoa(nums[j]) {
            n, _ := strconv.Atoi(string(r))
            sumJ += n
        }
        if sumI == sumJ {
            return nums[i] < nums[j]
        }
        return sumI < sumJ
    })
    return nums
}



