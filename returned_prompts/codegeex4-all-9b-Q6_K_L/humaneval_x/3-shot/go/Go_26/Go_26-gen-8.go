    result := make([]int, 0)
    for _, n := range numbers {
        found := false
        for _, r := range result {
            if r == n {
                found = true
                break
            }
        }
        if !found {
            result = append(result, n)
        }
    }
    return result
}



