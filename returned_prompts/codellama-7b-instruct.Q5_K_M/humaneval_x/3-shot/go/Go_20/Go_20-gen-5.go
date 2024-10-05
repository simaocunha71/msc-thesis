    var min_distance = math.Inf(1)
    var closest_pair [2]float64

    for i := 0; i < len(numbers) - 1; i++ {
        for j := i + 1; j < len(numbers); j++ {
            var distance = math.Abs(numbers[i] - numbers[j])
            if distance < min_distance {
                min_distance = distance
                closest_pair = [2]float64{numbers[i], numbers[j]}
            }
        }
    }
    return closest_pair
}



