    min_sum := math.MaxInt
    current_sum := 0
    for i := 0; i < len(nums); i++ {
        current_sum += nums[i]
        min_sum = math.Min(min_sum, current_sum)
        if current_sum < 0 {
            current_sum = 0
        }
    }
    return min_sum
}



