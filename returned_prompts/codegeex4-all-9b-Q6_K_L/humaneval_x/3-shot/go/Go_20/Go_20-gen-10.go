    var minDiff float64 = 1e20
    var result [2]float64
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var diff float64 = math.Abs(numbers[i] - numbers[j])
            if diff < minDiff {
                minDiff = diff
                result[0] = numbers[i]
                result[1] = numbers[j]
            }
        }
    }
    return result
}

