    var min, max float64
    min = numbers[0]
    max = numbers[0]
    for i := range numbers {
        if numbers[i] < min {
            min = numbers[i]
        }
        if numbers[i] > max {
            max = numbers[i]
        }
    }
    for i, v := range numbers {
        numbers[i] = (v - min) / (max - min)
    }
    return numbers
}


