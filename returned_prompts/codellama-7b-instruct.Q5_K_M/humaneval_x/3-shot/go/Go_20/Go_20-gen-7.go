    var closest_pair [2]float64
    closest_pair[0] = math.Inf(1)
    closest_pair[1] = math.Inf(-1)
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            distance := math.Abs(numbers[i] - numbers[j])
            if distance < closest_pair[1] - closest_pair[0] {
                closest_pair[0] = numbers[i]
                closest_pair[1] = numbers[j]
            }
        }
    }
    return closest_pair
}



