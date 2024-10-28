    result := make([]int,0)
    if len(numbers) == 0 {
        return result
    }

    for i := 0; i < len(numbers); i++ {
        result = append(result, numbers[i])
        if i < len(numbers) - 1 {
            result = append(result, delimeter)
        }
    }
    return result
}



