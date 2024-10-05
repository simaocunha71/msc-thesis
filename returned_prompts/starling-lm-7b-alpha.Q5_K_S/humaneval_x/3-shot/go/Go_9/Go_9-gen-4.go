    result := make([]int, len(numbers))
    max_until_now := numbers[0]
    for i := 0; i < len(numbers); i++ {
        if numbers[i] > max_until_now {
            max_until_now = numbers[i]
        }
        result[i] = max_until_now
    }
    return result
}



