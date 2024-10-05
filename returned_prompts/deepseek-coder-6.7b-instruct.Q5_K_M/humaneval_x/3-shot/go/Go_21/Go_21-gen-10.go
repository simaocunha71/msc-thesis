    min, max := minMax(numbers)
    diff := max - min
    result := make([]float64, len(numbers))
    for i, num := range numbers {
        result[i] = (num - min) / diff
    }
    return result
}

func minMax(numbers []float64) (float64, float64) {
    min := numbers[0]
    max := numbers[0]
    for _, num := range numbers {
        if num < min {
            min = num
        }
        if num > max {
            max = num
        }
    }
    return min, max
}



