    result := make([]int, 0)
    for _, n := range numbers {
        if len(result) == 0 || n != result[len(result)-1] {
            result = append(result, n)
        }
    }
    return result
}



