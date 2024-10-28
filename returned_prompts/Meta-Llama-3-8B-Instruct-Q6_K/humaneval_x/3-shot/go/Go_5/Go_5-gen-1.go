    result := make([]int, 0)
    for _, num := range numbers {
        result = append(result, num)
        result = append(result, delimeter)
    }
    return result[:len(result)-1]
}