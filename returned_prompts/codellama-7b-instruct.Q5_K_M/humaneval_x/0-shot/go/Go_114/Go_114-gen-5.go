    // Find the maximum subarray sum
    maxSum := math.MinInt64
    for i := 0; i < len(nums); i++ {
        curSum := 0
        for j := i; j < len(nums); j++ {
            curSum += nums[j]
            if curSum > maxSum {
                maxSum = curSum
            }
        }
    }
    return maxSum
}

B:
    // Find the minimum subarray sum
    minSum := math.MaxInt64
    for i := 0; i < len(nums); i++ {
        curSum := 0
        for j := i; j < len(nums); j++ {
            curSum += nums[j]
            if curSum < minSum {
                minSum = curSum
            }
        }
    }
    return minSum
}

C:
    // Find the minimum subarray sum
    minSum := math.MaxInt64
    for i := 0; i < len(nums); i++ {
        curSum := 0
        for j := i; j < len(nums); j++ {
            curSum += nums[j]
            if curSum < minSum {
                minSum = curSum
            }
        }
    }
    return minSum
}

D:
    // Find the minimum subarray sum
    minSum := math.MaxInt64
    for i := 0; i < len(nums); i++ {
        curSum := 0
        for j := i; j < len(nums); j++ {
            curSum += nums[j]
            if curSum < minSum {
                minSum = curSum
            }
        }
    }
    return minSum
}

E:
    // Find the minimum subarray sum
    minSum := math.MaxInt64
    for i := 0; i < len(nums); i++ {
        curSum := 0
        for j := i; j < len(nums); j++ {
            curSum += nums[j]
            if curSum < minSum {