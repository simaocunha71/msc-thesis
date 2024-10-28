    var min_distance float64 = math.MaxFloat64
    var min_index1 int = -1
    var min_index2 int = -1

    for i:= 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var current_distance float64 = math.Abs(numbers[i] - numbers[j])
            if current_distance < min_distance {
                min_distance = current_distance
                min_index1 = i
                min_index2 = j
            }
        }
    }

    return [2]float64{numbers[min_index1], numbers[min_index2]}
}



