    min_dist := math.Inf(1)
    first_index := 0
    second_index := 0

    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            dist := math.Abs(numbers[i] - numbers[j])
            if dist < min_dist {
                min_dist = dist
                first_index = i
                second_index = j
            }
        }
    }
    return [2]float64{numbers[first_index], numbers[second_index]}
}



