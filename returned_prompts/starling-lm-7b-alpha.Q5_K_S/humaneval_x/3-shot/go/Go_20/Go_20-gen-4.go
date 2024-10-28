    min_distance := math.Inf(1)
    result := [2]float64{math.Inf(1), math.Inf(-1)}

    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            distance := math.Abs(numbers[i] - numbers[j])
            if distance < min_distance {
                min_distance = distance
                result = [2]float64{numbers[i], numbers[j]}
            }
        }
    }
    return result
}



