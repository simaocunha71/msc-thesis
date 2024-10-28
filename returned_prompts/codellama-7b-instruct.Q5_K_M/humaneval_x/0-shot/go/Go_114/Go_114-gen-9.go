    for i := 0; i < len(nums); i++ {
        sum := 0
        for j := i; j < len(nums); j++ {
            sum += nums[j]
            if sum < 0 {
                sum = 0
                break
            }
            if sum == 0 {
                return 0
            }
        }
    }
    return math.MaxInt32
}


