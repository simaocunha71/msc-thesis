    min_sum = math.MinInt32
    current_sum = 0

    for _, num := range nums {
        current_sum += num
        if current_sum < min_sum {
            min_sum = current_sum
        }
        if current_sum < 0 {
            current_sum = 0
        }
    }
    return min_sum
}