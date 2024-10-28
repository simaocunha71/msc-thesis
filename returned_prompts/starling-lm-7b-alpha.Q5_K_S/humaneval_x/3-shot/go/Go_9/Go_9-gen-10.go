    result := make([]int, len(numbers))
    result[0] = numbers[0]
    current_max := result[0]

    for i := 1; i < len(numbers); i++ {
        if numbers[i] > current_max {
            current_max = numbers[i]
        }
        result[i] = current_max
    }
    return result
}



