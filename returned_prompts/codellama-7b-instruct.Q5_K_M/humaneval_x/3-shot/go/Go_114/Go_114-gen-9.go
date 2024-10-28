    min_sum := math.MaxInt32

    for i := 0; i < len(nums); i++ {
        curr_sum := 0
        for j := i; j < len(nums); j++ {
            curr_sum += nums[j]
            if curr_sum < min_sum {
                min_sum = curr_sum
            }
        }
    }
    return min_sum
}



