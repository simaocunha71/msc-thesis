    result := make([]int, 0)

    for _, num := range numbers {
        if !Contains(result, num) {
            result = append(result, num)
        }
    }
    return result
}



