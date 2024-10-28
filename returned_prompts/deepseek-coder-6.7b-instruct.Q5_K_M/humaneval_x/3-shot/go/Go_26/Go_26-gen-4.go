    result := make([]int, 0, len(numbers))
    seen := make(map[int]bool)
    for _, num := range numbers {
        if seen[num] {
            continue
        }
        result = append(result, num)
        seen[num] = true
    }
    return result
}



