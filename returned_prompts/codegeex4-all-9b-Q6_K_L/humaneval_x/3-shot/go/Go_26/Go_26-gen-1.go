    seen := make(map[int]bool)
    result := make([]int, 0)

    for _, n := range numbers {
        if !seen[n] {
            seen[n] = true
            result = append(result, n)
        }
    }

    return result
}

