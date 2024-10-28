    result := make([]int, len(numbers))
    max := numbers[0]
    result[0] = max
    for i := 1; i < len(numbers); i++ {
        if numbers[i] > max {
            max = numbers[i]
        }
        result[i] = max
    }
    return result
}



