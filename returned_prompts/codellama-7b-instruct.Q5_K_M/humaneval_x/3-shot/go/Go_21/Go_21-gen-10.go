    min := numbers[0]
    max := numbers[0]
    for i := 0; i < len(numbers); i++ {
        if numbers[i] < min {
            min = numbers[i]
        }
        if numbers[i] > max {
            max = numbers[i]
        }
    }
    result := make([]float64, len(numbers))
    for i := 0; i < len(numbers); i++ {
        result[i] = (numbers[i] - min) / (max - min)
    }
    return result
}



