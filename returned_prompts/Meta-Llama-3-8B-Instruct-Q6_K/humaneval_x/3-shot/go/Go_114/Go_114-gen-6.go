    minSum := math.MaxInt32
    currSum := 0
    for _, num := range nums {
        currSum += num
        minSum = int(math.Min(float64(minSum), float64(currSum)))
        if currSum < 0 {
            currSum = 0
        }
    }
    return minSum
}