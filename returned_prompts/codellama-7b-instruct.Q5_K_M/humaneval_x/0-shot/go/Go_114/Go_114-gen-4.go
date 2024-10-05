    // O(N)
    // O(1)
    minSum := math.MaxInt32
    for i := 0; i < len(nums); i++ {
        sum := 0
        for j := i; j < len(nums); j++ {
            sum += nums[j]
            minSum = min(minSum, sum)
        }
    }
    return minSum
}

func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}
