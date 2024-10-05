    result := int(math.Pow(10,float64(n)))
    if n > 1 {
        result -= int(math.Pow(10,float64(n-1)))
    }
    return result
}



