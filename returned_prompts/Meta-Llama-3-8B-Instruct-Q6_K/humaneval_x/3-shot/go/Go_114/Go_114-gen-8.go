    min_sum := math.MaxInt32
    current_sum := 0

    for _, num := range nums {
        current_sum += num
        min_sum = min(min_sum, current_sum)
        if current_sum < 0 {
            current_sum = 0
        }
    }
    return min_sum
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}