    min_diff := math.MaxFloat64
    closest_nums := [2]float64{-math.MaxFloat64, -math.MaxFloat64}

    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var diff float64 = math.Abs(numbers[i] - numbers[j])
            if diff < min_diff {
                min_diff = diff
                closest_nums[0] = numbers[i]
                closest_nums[1] = numbers[j]
            }
        }
    }
    return closest_nums
}
}  // End of package main.