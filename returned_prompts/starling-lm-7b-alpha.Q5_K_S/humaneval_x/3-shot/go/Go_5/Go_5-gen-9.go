    result := make([]int, 0)
    result = append(result, numbers[0])
    for _, n := range numbers[1:] {
        result = append(result, delimeter)
        result = append(result, n)
    }
    return result
}




