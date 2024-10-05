    result := make([]int, 0)
    for _, n := range numbers {
        result = append(result, n)
        result = append(result, delimeter)
    }
    return result
}



