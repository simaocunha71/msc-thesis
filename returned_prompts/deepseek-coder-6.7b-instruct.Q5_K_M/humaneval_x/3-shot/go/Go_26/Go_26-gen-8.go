    result := make([]int, 0)
    seen := make(map[int]bool)

    for _, number := range numbers {
        if _, ok := seen[number]; !ok {
            result = append(result, number)
            seen[number] = true
        }
    }
    return result
}



