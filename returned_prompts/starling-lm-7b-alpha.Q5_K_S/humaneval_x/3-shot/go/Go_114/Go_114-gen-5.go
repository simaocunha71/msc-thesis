    result := math.MaxInt32
    sum := 0
    for _, num := range nums {
        sum += num
        result = min(result, sum)
        if sum < 0 {
            sum = 0
        }
    }
    return result
}



