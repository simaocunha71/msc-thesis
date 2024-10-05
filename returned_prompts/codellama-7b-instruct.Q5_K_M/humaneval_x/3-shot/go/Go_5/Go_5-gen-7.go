    result := make([]int, 0, len(numbers) * 2 - 1)

    for i := 0; i < len(numbers); i++ {
        if i > 0 {
            result = append(result, delimeter)
        }
        result = append(result, numbers[i])
    }
    return result
}



