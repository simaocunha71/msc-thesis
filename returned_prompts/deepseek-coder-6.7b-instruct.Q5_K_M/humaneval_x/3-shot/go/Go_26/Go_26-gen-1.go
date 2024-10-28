    seen := make(map[int]bool)
    result := make([]int, 0)
    for _, num := range numbers {
        if _, ok := seen[num]; !ok {
            seen[num] = true
            result = append(result, num)
        }
    }
    return result
}



