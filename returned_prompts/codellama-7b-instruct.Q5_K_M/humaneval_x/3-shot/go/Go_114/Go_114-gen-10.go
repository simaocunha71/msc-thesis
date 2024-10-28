    min_sum := math.MaxInt
    sum := 0
    for i := 0; i < len(nums); i++ {
        sum += nums[i]
        min_sum = int(math.Min(float64(min_sum), float64(sum)))
        if sum < min_sum {
            min_sum = sum
        }
        if sum > 0 {
            sum = 0
        }
    }
    return min_sum
}



