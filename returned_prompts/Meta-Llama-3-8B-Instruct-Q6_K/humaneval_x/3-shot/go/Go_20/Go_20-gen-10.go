    min_diff := math.MaxFloat64
    result := [2]float64{}

    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var diff float64 = math.Abs(numbers[i] - numbers[j])
            if diff < min_diff {
                min_diff = diff
                result[0] = numbers[i]
                result[1] = numbers[j]
            }
        }
    }
    return result
}