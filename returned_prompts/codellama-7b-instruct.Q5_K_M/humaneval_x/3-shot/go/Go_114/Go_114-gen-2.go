    result := nums[0]
    current_sum := nums[0]
    for i := 1; i < len(nums); i++ {
        current_sum = min(current_sum + nums[i], nums[i])
        result = min(result, current_sum)
    }
    return result
}



