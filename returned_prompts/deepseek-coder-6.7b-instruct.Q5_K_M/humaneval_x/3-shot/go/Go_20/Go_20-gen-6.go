    min_diff := math.MaxFloat64
    result := [2]float64{}

    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            diff := math.Abs(numbers[i] - numbers[j])
            if diff < min_diff {
                min_diff = diff
                if numbers[i] < numbers[j] {
                    result[0] = numbers[i]
                    result[1] = numbers[j]
                } else {
                    result[0] = numbers[j]
                    result[1] = numbers[i]
                }
            }
        }
    }
    return result
}



