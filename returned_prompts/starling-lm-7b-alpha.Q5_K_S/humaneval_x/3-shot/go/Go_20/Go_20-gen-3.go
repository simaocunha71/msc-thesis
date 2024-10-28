    min_diff := math.MaxFloat64
    min_elements := [2]float64{0,0}
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            diff := math.Abs(numbers[i] - numbers[j])
            if diff < min_diff {
                min_diff = diff
                min_elements = [2]float64{numbers[i],numbers[j]}
            }
        }
    }
    return min_elements
}



