    if len(arr)==0 {
        return nil
    }
    result := 1
    for _, i := range arr {
        result *= i
    }
    return math.Abs(float64(result))
}



