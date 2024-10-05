    result := make([]int, 0)

    for i, n := range numbers {
        result = append(result, n)

        if i < len(numbers) - 1 {
            result = append(result, delimeter)
        }
    }
    return result
}



