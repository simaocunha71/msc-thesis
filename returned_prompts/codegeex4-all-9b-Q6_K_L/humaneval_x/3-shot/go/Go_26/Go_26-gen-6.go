    seen := make(map[int]bool)
    var result []int

    for _, num := range numbers {
        if _, ok := seen[num]; !ok {
            seen[num] = true
            result = append(result, num)
        }
    }

    return result
}



