    result := math.MaxInt32
    current := math.MaxInt32
    for _, n := range nums {
        current = int(math.Min(float64(n), float64(current + n)))
        result = int(math.Min(float64(result), float64(current)))
    }
    return result
}



