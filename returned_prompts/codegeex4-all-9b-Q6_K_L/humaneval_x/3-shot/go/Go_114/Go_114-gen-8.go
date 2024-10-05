    min_sum := math.MaxInt64
    for i := 0; i < len(nums); i++ {
        for j := i + 1; j <= len(nums); j++ {
            current_sum := 0
            for k := i; k < j; k++ {
                current_sum += nums[k]
            }
            if current_sum < min_sum {
                min_sum = current_sum
            }
        }
    }
    return min_sum
}



