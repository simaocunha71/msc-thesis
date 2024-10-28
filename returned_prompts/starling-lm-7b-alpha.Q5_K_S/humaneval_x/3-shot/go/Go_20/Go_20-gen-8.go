    min := math.MaxFloat64
    min_index := 0
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i] - numbers[j]) < min {
                min = math.Abs(numbers[i] - numbers[j])
                min_index = i
            }
        }
    }
    return [2]float64{numbers[min_index], numbers[(min_index + 1) % len(numbers)]}
}



