    maxNum := math.MinInt64
    result := make([]int, len(numbers))

    for i, num := range numbers {
        if num > maxNum {
            maxNum = num
        }
        result[i] = maxNum
    }
    return result
}

