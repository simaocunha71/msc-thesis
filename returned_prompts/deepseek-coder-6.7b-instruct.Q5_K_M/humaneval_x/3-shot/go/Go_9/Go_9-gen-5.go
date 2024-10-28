    max_value := 0
    result := make([]int, len(numbers))

    for i, number := range numbers {
        if number > max_value {
            max_value = number
        }
        result[i] = max_value
    }

    return result
}



