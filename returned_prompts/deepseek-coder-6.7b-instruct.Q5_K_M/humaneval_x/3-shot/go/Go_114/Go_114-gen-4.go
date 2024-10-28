    min_sum := int(math.Pow(2, 63) - 1)
    n := len(nums)

    for i := 0; i < n; i++ {
        sum := 0
        for j := i; j < n; j++ {
            sum += nums[j]
            if sum < min_sum {
                min_sum = sum
            }
        }
    }

    return min_sum
}



