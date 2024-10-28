    var closest_pair [2]float64
    closest_pair[0] = numbers[0]
    closest_pair[1] = numbers[0]

    for i := 1; i < len(numbers); i++ {
        for j := 0; j < i; j++ {
            if math.Abs(numbers[i] - numbers[j]) < math.Abs(closest_pair[1] - closest_pair[0]) {
                closest_pair[0] = numbers[j]
                closest_pair[1] = numbers[i]
            }
        }
    }
    return closest_pair
}



