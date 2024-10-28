    min := math.MaxInt32
    for i := 0; i < len(nums); i++ {
        sum := 0
        for j := i; j < len(nums); j++ {
            sum += nums[j]
            if sum < min {
                min = sum
            }
        }
    }
    return min
}



