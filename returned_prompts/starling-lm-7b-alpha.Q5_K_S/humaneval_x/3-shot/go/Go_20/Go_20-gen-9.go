    min_diff := math.MaxFloat64
    a, b := 0.0, 0.0
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            diff := math.Abs(numbers[i] - numbers[j])
            if diff < min_diff {
                min_diff = diff
                a = numbers[i]
                b = numbers[j]
            }
        }
    }
    return [2]float64{a, b}
}



