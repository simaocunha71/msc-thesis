    sort.SliceStable(nums, func(i, j int) bool {
        sum_i := 0
        sum_j := 0
        for _, r := range strconv.Itoa(nums[i]) {
            n, _ := strconv.Atoi(string(r))
            sum_i += n
        }
        for _, r := range strconv.Itoa(nums[j]) {
            n, _ := strconv.Atoi(string(r))
            sum_j += n
        }
        return sum_i < sum_j
    })
    return nums
}



