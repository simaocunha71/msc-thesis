    for i := 0; i < len(nums); i++ {
        for j := i; j < len(nums); j++ {
            sum := 0
            for k := i; k <= j; k++ {
                sum += nums[k]
            }
            if sum < 0 {
                continue A
            }
        }
    }
    return 0
}


