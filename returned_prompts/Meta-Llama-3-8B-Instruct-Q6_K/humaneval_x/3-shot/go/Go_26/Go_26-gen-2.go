    result := make([]int, 0)
    seen := make(map[int]bool)

    for _, num := range numbers {
        if !seen[num] {
            seen[num] = true
            result = append(result, num)
        }
    }
    return result
}