    result := make([]int, 0)
    if len(numbers) == 0 {
        return result
    }
    result = append(result, numbers[0])
    for i := 1; i < len(numbers); i++ {
        result = append(result, delimeter)
        result = append(result, numbers[i])
    }
    return result
}



