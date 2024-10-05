    result := make([]int, 0)
    appearances := make(map[int]bool)

    for _, number := range numbers {
        if _, seen := appearances[number]; !seen {
            appearances[number] = true
            result = append(result, number)
        }
    }

    return result
}



