    result := make([]int, 0)
    current_max := 0

    for _, num := range numbers {
        if num > current_max {
            current_max = num
        }
        result = append(result, current_max)
    }
    return result
}



