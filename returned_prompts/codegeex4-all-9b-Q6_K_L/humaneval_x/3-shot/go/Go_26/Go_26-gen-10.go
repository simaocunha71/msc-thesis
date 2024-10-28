    result := make([]int, 0)

    for _, number := range numbers {
        found := false
        for _, r := range result {
            if number == r {
                found = true
                break
            }
        }
        if !found {
            result = append(result, number)
        }
    }
    return result
}



