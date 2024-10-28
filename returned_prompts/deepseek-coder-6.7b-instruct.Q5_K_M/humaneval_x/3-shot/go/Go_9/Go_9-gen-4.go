    max_num := math.MinInt64
    result := make([]int, len(numbers))

    for i, num := range numbers {
        if num > max_num {
            max_num = num
        }
        result[i] = max_num
    }

    return result
}



