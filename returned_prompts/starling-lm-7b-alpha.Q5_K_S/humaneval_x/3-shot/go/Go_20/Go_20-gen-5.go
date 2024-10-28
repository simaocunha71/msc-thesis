    min_difference := float64(math.MaxFloat64)
    min_pair := [2]float64{math.MaxFloat64, math.MaxFloat64}
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            difference := math.Abs(numbers[i] - numbers[j])
            if difference < min_difference {
                min_difference = difference
                min_pair[0] = numbers[i]
                min_pair[1] = numbers[j]
            }
        }
    }
    return min_pair
}



