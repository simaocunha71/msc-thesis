    result := math.MaxInt64

    min_sum := 0
    for _, num := range nums {
        min_sum += num
        if min_sum < result {
            result = min_sum
        }
        if min_sum < 0 {
            min_sum = 0
        }
    }
    return result
}



