    result := make([]int, 0)
    last_seen := make(map[int]bool)
    for _, n := range numbers {
        if !last_seen[n] {
            result = append(result, n)
            last_seen[n] = true
        }
    }
    return result
}



