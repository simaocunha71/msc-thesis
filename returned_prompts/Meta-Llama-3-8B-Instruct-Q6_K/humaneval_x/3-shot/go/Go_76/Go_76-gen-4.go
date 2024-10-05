    if x <= 0 || n <= 0 {
        return false
    }
    log := math.Log(float64(x)) / math.Log(float64(n))
    return math.Mod(log, 1) == 0
}  // or return math.Abs(log - math.Floor(log)) < 1e-9