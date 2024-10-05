    var result [2]float64
    var min_distance float64 = math.MaxFloat64

    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var distance float64 = math.Abs(numbers[i] - numbers[j])
            if distance < min_distance {
                min_distance = distance
                result[0] = numbers[i]
                result[1] = numbers[j]
            }
        }
    }
    return result
}



