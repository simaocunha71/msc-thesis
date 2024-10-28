    result := make([]int, len(numbers))
    result[0] = numbers[0]
    max_so_far := numbers[0]

    for i := 1; i < len(numbers); i++ {
        if numbers[i] > max_so_far {
            max_so_far = numbers[i]
        }
        result[i] = max_so_far
    }
    return result
}