    min := math.MaxInt32
    for i := 0; i < len(nums); i++ {
        current_sum := 0
        for j := i; j < len(nums); j++ {
            current_sum += nums[j]
            if current_sum < min {
                min = current_sum
            }
        }
    }
    return min
}



