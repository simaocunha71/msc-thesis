    result := make([]int, 0)
    seen := make(map[int]bool)
    for _, num := range numbers {
        if _, ok := seen[num]; !ok {
            result = append(result, num)
            seen[num] = true
        }
    }
    return result
}



