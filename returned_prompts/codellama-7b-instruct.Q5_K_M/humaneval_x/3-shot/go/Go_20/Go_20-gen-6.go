    min_diff := math.Inf(+1)
    idx1 := 0
    idx2 := 0

    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            diff := math.Abs(numbers[i] - numbers[j])
            if diff < min_diff {
                min_diff = diff
                idx1 = i
                idx2 = j
            }
        }
    }
    return [2]float64{numbers[idx1], numbers[idx2]}
}



