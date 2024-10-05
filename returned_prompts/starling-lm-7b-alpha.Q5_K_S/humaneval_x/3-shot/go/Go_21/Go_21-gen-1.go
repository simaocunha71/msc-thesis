    var min, max float64 = math.Max(numbers[0],numbers[1]), math.Min(numbers[0],numbers[1])

    for _,i := range numbers{
        if i < min {
            min = i
        }
        if i > max {
            max = i
        }
    }

    result := make([]float64,0)
    for _,i := range numbers {
        result = append(result, (i-min)/(max-min))
    }

    return result
}



