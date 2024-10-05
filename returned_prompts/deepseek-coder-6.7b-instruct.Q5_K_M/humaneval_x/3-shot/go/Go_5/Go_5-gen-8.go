    result := make([]int, 0, len(numbers)*2-1)
    for i, number := range numbers {
        result = append(result, number)
        if i < len(numbers)-1 {
            result = append(result, delimeter)
        }
    }
    return result
}



