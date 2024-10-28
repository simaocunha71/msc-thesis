    sort.Slice(nums, func(i, j int) bool {
        sumI := 0
        sumJ := 0
        for _, v := range strconv.Itoa(nums[i]) {
            n, _ := strconv.Atoi(string(v))
            sumI += n
        }
        for _, v := range strconv.Itoa(nums[j]) {
            n, _ := strconv.Atoi(string(v))
            sumJ += n
        }
        if sumI == sumJ {
            return i < j
        }
        return sumI < sumJ
    })

    return nums
}



