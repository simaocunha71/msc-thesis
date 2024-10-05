    min_sum := nums[0]
    current_sum := nums[0]

    for i := 1; i < len(nums); i++ {
        current_sum = int(math.Min(float64(current_sum + nums[i]), float64(nums[i])))
        min_sum = int(math.Min(float64(min_sum), float64(current_sum)))
    }

    return min_sum
}



