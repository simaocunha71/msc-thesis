    result := 0
    for _, i := range arr {
        if TruncateNumber(math.Abs(float64(i))) > 0 {
            result += 1
        }
    }
    return result
}



