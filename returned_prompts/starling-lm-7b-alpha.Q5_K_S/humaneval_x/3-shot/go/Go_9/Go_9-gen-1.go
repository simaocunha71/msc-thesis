    result := make([]int, len(numbers))
    current_max := numbers[0]
    result[0] = current_max

    for i := 1; i < len(numbers); i++ {
        current_max = max(numbers[i], current_max)
        result[i] = current_max
    }
    return result
}



