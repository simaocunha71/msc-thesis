    result := make([]int, len(numbers))
    max := numbers[0]
    result[0] = max
    for i, n := range numbers[1:] {
        if n > max {
            max = n
        }
        result[i+1] = max
    }
    return result
}



