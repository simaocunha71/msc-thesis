    var current_sum int
    var min_sum int = math.MaxInt32

    for i := 0; i < len(nums); i++ {
        current_sum += nums[i]
        for current_sum < 0 {
            current_sum += nums[i]
            i++
        }
        min_sum = int(math.Min(float64(min_sum), float64(current_sum)))
    }

    return min_sum
}



