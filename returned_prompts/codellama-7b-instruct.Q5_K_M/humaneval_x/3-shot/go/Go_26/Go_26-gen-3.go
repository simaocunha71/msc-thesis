    result := make([]int, 0)
    for _, n := range numbers {
        if !Contains(result, n) {
            result = append(result, n)
        }
    }
    return result
}



