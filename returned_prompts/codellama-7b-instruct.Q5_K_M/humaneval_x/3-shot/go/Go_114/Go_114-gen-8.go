    result := math.MaxInt32
    current_sum := 0

    for i := 0; i < len(nums); i++ {
        current_sum += nums[i]
        result = int(math.Min(float64(result), float64(current_sum)))

        if current_sum < 0 {
            current_sum = 0
        }
    }
    return result
}



