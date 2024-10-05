    result := math.MaxInt32
    current_sum := 0

    for _, num := range nums {
        current_sum += num
        if current_sum < result {
            result = current_sum
        }
        if current_sum < 0 {
            current_sum = 0
        }
    }
    return result
}



