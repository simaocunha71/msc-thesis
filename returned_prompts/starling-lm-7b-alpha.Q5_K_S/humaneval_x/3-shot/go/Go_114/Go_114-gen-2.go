    result := math.MaxInt64
    curr_sum := 0
    for _, num := range nums {
        curr_sum += num
        result = min(result, curr_sum)
        if curr_sum < 0 {
            curr_sum = 0
        }
    }
    return result
}



