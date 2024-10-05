    result := make([]int, 0)
    seen := make(map[int]bool)

    for _, x := range numbers {
        if !seen[x] {
            seen[x] = true
            result = append(result, x)
        }
    }
    return result
}



