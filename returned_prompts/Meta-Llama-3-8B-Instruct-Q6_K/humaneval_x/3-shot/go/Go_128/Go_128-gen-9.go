    if len(arr) == 0 {
        return nil
    }
    var prod float64 = 1.0
    var sum float64 = 0.0
    for _, val := range arr {
        if val == 0 {
            return 0
        }
        prod *= math.Signbit(float64(val))
        sum += math.Abs(float64(val))
    }
    return sum * prod
}