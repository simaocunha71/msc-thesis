    min_sum := 0
    for i := 0; i < len(nums); i++ {
        min_sum += nums[i]
        if min_sum < 0 {
            min_sum = 0
        }
    }
    return min_sum
}



