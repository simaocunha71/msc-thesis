    var closest_distance float64 = 1000000
    var closest_pair [2]float64

    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var distance float64 = math.Abs(numbers[i] - numbers[j])
            if distance < closest_distance {
                closest_distance = distance
                closest_pair[0] = numbers[i]
                closest_pair[1] = numbers[j]
            }
        }
    }
    return closest_pair
}