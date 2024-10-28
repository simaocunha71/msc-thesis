    result := make([]int, 0, len(numbers)+len(numbers)-1)
    result = append(result, numbers[0])
    for i := 1; i < len(numbers); i++ {
        result = append(result, delimeter)
        result = append(result, numbers[i])
    }
    return result
}