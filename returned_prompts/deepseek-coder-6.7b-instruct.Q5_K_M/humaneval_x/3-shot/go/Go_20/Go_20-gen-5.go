    sort.Float64s(numbers)
    var min_diff float64 = math.MaxFloat64
    var result [2]float64

    for i  := 0; i  len(numbers) - 1; i++  {
        var diff float64 = numbers[i+1] - numbers[i]
        if diff < min_diff  {
            min_diff = diff
            result[0] = numbers[i]
            result[1] = numbers[i+1]
         }
     }
    return result
}



