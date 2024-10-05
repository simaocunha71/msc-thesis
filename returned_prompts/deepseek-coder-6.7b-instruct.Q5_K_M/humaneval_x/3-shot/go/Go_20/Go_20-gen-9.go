    sort.Float64s(numbers)
    min_difference := math.MaxFloat64
    result := [2]float64{}

    for i:=0; i<len(numbers)-1; i++ {
        difference := numbers[i+1] - numbers[i]
        if difference < min_difference {
            min_difference = difference
            result[0] = numbers[i]
            result[1] = numbers[i+1]
        }
    }
    return result
}



