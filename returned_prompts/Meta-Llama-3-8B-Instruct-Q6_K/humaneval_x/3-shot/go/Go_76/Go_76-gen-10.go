    if n <= 0 {
        return false
    }
    base := int(math.Pow(float64(n), math.Floor(math.Log(float64(x))/math.Log(float64(n)))))
    return base == x
}