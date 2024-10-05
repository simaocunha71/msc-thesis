    min  := numbers[0]
    max  := numbers[0]
    for _, number := range numbers {
        if number < min {
            min = number
        }
        if number > max {
            max = number
        }
    }

    range_  := max - min

    result  := make([]float64, len(numbers))
    for i, number := range numbers {
        result[i] = (number - min) / range_
    }

    return result
}



