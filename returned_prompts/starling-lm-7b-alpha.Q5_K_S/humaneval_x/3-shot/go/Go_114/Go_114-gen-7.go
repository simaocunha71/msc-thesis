    result := math.MaxInt32
    for i := 0; i < len(nums); i++ {
        var current_sum int = 0
        for j := i; j < len(nums); j++ {
            current_sum += nums[j]
            result = min(result, current_sum)
        }
    }
    return result
}



