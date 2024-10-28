    result := make([]int, 0)
    max := numbers[0]

    for _, num := range numbers {
        if num > max {
            max = num
        }
        result = append(result, max)
    }
    return result
}