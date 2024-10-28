    min := numbers[0]
    max := numbers[0]
    for _, number := range numbers {
        if number < min {
            min = number
        }
        if number > max {
            max = number
        }
    }

    result := make([]float64, len(numbers))
    for i, number := range numbers {
        result[i] = (number - min) / (max - min)
    }
    return result
}



