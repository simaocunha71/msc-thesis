    min_sum := math.MaxInt32
    sum := 0
    for i := 0; i < len(nums); i++ {
        sum += nums[i]
        for sum < 0 && i < len(nums) {
            sum += nums[i]
            i += 1
        }
        if sum < min_sum {
            min_sum = sum
        }
    }
    return min_sum
}



