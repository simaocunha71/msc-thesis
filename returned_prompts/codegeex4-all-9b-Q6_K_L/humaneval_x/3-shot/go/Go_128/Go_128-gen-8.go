    if len(arr) == 0 {
        return nil
    }

    var result float64 = 1
    for _, num := range arr {
        result *= float64(math.Abs(float64(num)))
    }
    return result
}



