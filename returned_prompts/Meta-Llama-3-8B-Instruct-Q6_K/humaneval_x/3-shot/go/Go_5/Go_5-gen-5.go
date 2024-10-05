    result := make([]int, 0, len(numbers)*2 - 1)
    for i := 0; i < len(numbers); i++ {
        result = append(result, numbers[i])
        if i < len(numbers) - 1 {
            result = append(result, delimeter)
        }
    }
    return result
}