    result := make([]int, 0)
    visited := make(map[int]bool)

    for _, n := range numbers {
        if !visited[n] {
            visited[n] = true
            result = append(result, n)
        }
    }
    return result
}



