    result := make([]int, 0)
    indexes := make(map[int]bool)

    for _, n := range numbers {
        if !indexes[n] {
            result = append(result, n)
            indexes[n] = true
        }
    }
    return result
}



