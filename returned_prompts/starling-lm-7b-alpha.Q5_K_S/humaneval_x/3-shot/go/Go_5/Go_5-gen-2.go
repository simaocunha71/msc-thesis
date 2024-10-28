    result := make([]int, 0)
    for _, number := range numbers {
        result = append(result, number)
        result = append(result, delimeter)
    }
    return result
}



