    min := math.Min(float64(numbers[0]),math.Min(float64(numbers[1]),math.Min(float64(numbers[2]),math.Min(float64(numbers[3]),math.Min(float64(numbers[4]),float64(numbers[5]))))))
    max := math.Max(float64(numbers[0]),math.Max(float64(numbers[1]),math.Max(float64(numbers[2]),math.Max(float64(numbers[3]),math.Max(float64(numbers[4]),float64(numbers[5]))))))
    result := make([]float64, len(numbers))
    for i := 0; i < len(numbers); i++ {
        result[i] = (numbers[i] - min) / (max - min)
    }
    return result
}