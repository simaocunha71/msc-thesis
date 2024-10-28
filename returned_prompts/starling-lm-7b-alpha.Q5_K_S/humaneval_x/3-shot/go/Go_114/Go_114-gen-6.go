    minSum := math.MaxInt32
    currentSum := 0
    for _, num := range nums {
        currentSum += num
        if currentSum < 0 {
            currentSum = 0
        } else if currentSum < minSum {
            minSum = currentSum
        }
    }
    return minSum
}



