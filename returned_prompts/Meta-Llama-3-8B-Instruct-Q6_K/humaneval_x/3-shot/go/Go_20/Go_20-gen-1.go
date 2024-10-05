    var min_diff float64 = math.MaxFloat64
    var closest_pair [2]float64

    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var diff float64 = math.Abs(numbers[i] - numbers[j])
            if diff < min_diff {
                min_diff = diff
                closest_pair[0] = numbers[i]
                closest_pair[1] = numbers[j]
            }
        }
    }
    return closest_pair
}

