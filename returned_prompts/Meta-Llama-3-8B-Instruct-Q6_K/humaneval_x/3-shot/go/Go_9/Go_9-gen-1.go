    result := make([]int, len(numbers))
    result[0] = numbers[0]
    max := numbers[0]
    for i := 1; i < len(numbers); i++ {
        if numbers[i] > max {
            max = numbers[i]
        }
        result[i] = max
    }
    return result
}
