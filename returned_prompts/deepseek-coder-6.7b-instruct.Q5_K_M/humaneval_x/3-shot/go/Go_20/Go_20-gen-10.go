    sort.Float64s(numbers)
    var min_difference float64  = math.MaxFloat64
    var closest_pair [2]float64

    for i  := 0; i < len(numbers) - 1; i++  {
        var difference float64  = numbers[i+1] - numbers[i]
        if difference < min_difference  {
            min_difference  = difference
            closest_pair  = [2]float64{numbers[i], numbers[i+1]}
        }
     }

     return closest_pair
 }


