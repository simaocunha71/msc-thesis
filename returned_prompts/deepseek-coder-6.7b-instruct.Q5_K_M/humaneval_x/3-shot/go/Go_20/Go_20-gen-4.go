    sort.Float64s(numbers)
    minDiff := math.MaxFloat64
    result := [2]float64{}

    for i := 0; i < len(numbers)-1; i++ {
        if diff := numbers[i+1] - numbers[i]; diff < minDiff {
            minDiff = diff
            result[0] = numbers[i]
            result[1] = numbers[i+1]
        }
    }

    return result
}



