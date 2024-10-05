    result := make([]int, len(numbers))
    max := 0
    for i, n := range numbers {
        if n > max {
            max = n
        }
        result[i] = max
    }
    return result
}



