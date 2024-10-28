    sort.Float64s(numbers)
    min_diff := math.MaxFloat64
    result := [2]float64{}

    for i := 0; i < len(numbers)-1; i++ {
        if diff := numbers[i+1] - numbers[i]; diff < min_diff {
            min_diff = diff
            result[0] = numbers[i]
            result[1] = numbers[i+1]
        }
    }

    return result
}



