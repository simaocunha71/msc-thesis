    result := make([]int, len(numbers))
    for i := 0; i < len(numbers); i++ {
        result[i] = numbers[i]
        for j := i - 1; j >= 0 && numbers[j] < numbers[i]; j-- {
            result[j] = numbers[i]
        }
    }
    return result
}



