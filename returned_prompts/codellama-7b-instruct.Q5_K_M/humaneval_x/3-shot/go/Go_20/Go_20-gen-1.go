    min_diff := math.MaxFloat64
    min_diff_index := 0
    min_diff_index_2 := 0

    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            diff := math.Abs(numbers[i] - numbers[j])
            if diff < min_diff {
                min_diff = diff
                min_diff_index = i
                min_diff_index_2 = j
            }
        }
    }

    return [2]float64{numbers[min_diff_index], numbers[min_diff_index_2]}
}



