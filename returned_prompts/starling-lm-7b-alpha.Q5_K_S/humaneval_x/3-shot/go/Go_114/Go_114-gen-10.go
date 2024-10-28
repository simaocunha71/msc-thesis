    result := math.MaxInt32
    for i := 0; i < len(nums); i++ {
        current_sum := 0
        for j := i; j < len(nums); j++ {
            current_sum += nums[j]
            if current_sum < result {
                result = current_sum
            }
        }
    }
    return result
}



